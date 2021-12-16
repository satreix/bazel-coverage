load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_test")

def py_unittest(name, deps = None, **kwargs):
    """Declares a `unittest`-based python test.
    This macro should be preferred instead of the basic py_test for tests
    that use the `unittest` framework. Tests that use this macro should *not*
    contain a __main__ handler nor a shebang line.
    """
    helper = "//tools/build/python:py_unittest_main.py"
    if kwargs.pop("srcs", None):
        fail("Changing srcs is not allowed by py_unittest. Use py_test instead.")
    py_test(
        name = name,
        srcs = ["%s.py" % name, helper],
        main = helper,
        deps = (deps or []) + [
            "//tools/coverage/python:coverage",
            requirement("xmlrunner"),
        ],
        **kwargs
    )
