"""This is Stirling's default main() for unittest-based tests.  It is intended
for use by the py_unittest macro defined in //tools/build/python:defs.bzl and
should NOT be called directly by anything else.
"""

import io
import logging
import os
import re
import sys
import unittest
from importlib.machinery import SourceFileLoader

import xmlrunner

from tools.coverage.python.coverage import coverage_decorator


def main():
    # Obtain the full path for this test case; it looks a bit like this:
    # .../execroot/.../foo_test.runfiles/.../py_unittest_main.py
    main_py = sys.argv[0]

    workspace = os.environ["TEST_WORKSPACE"]

    # Parse the test case name out of the runfiles directory name.
    match = re.search("^(.*bin/(.*?/)?(py/)?([^/]*_test).runfiles/)", main_py)
    if not match:
        print("error: no test name match in {}".format(main_py))
        sys.exit(1)
    runfiles, test_package, _, test_name, = match.groups()
    test_basename = test_name + ".py"

    # Check the test's source code for a (misleading) __main__.
    test_repo_path = os.path.join(test_package, test_basename)
    runfiles_test_filename = os.path.join(runfiles, workspace, test_repo_path)
    if not os.path.exists(runfiles_test_filename):
        raise RuntimeError(f"Could not find {test_basename} at {runfiles_test_filename}")
    realpath_test_filename = os.path.realpath(runfiles_test_filename)
    with io.open(realpath_test_filename, "r", encoding="utf8") as infile:
        for line in infile.readlines():
            if any([line.startswith("if __name__ =="),
                    line.strip().startswith("unittest.main")]):
                logging.error(
                    f"{test_repo_path} appears to have a main "
                    "function (checks 'if __name__ == ') or call the main "
                    "function of unittest ('unittest.main') but also uses "
                    "py_unittest; when using py_unittest, "
                    "the boilerplate main function should not be used; "
                    "if this test is not based on unittest, declare it "
                    "as py_test instead of py_unittest and "
                    "keep the main function intact",
                )
                sys.exit(1)
    if os.access(realpath_test_filename, os.X_OK):
        if os.getcwd().startswith("/runner"):
            # Bazel side error. Bazel unconditionally sets +x for RBE files.
            # The following commit should (tm) fix this issue:
            # https://github.com/bazelbuild/bazel/commit/b6e3ba8abf033c6d3a318be8484021eff6a40dde
            logging.warning("IN RBE, the executable guard does not work yet")
        else:
            logging.error(
                f"{test_repo_path} uses py_unittest but is marked executable in "
                f"the filesystem; fix this via chmod a-x {test_repo_path}"
            )
            sys.exit(1)

    module = SourceFileLoader(test_name, runfiles_test_filename).load_module(
        test_name)

    # Figure out which arguments are for unittest and which are for the module
    # under test.
    unittest_argv = sys.argv[:1]
    known_unittest_args = [
        "-h", "--help",
        "-v", "--verbose",
        "-q", "--quiet",
        "-f", "--failfast",
        "-c", "--catch",
        "-b", "--buffer",
    ]
    test_class_guesses = [
        x for x in dir(module)
        if x.startswith("Test")
    ]
    index = 1
    while index < len(sys.argv):
        arg = sys.argv[index]
        if arg in known_unittest_args or any([
            arg.startswith(clazz) for clazz in test_class_guesses]):
            unittest_argv.append(arg)
            sys.argv.pop(index)
            continue
        index += 1

    # Delegate the rest to unittest.
    #
    # Use `warnings=False` to tell unittest to keep its hands off of our
    # warnings settings, exploting a loophole where it checks "if warnings
    # is None" to check if the user passed a kwarg, but "if warning" to
    # actually apply the user's kwarg.
    if "XML_OUTPUT_FILE" in os.environ:
        with open(os.environ["XML_OUTPUT_FILE"], "w") as output:
            unittest.main(
                module=test_name, argv=unittest_argv, warnings=False,
                testRunner=xmlrunner.XMLTestRunner(output=output),
                failfast=False,
                buffer=False,
                catchbreak=False,
            )
    else:
        unittest.main(module=test_name, argv=unittest_argv, warnings=False)


if __name__ == '__main__':
    with coverage_decorator():
        main()
