import contextlib
import os
import pathlib
import sys

import coverage
import coverage_lcov.converter


@contextlib.contextmanager
def coverage_decorator():
    if os.getenv("COVERAGE", None) == "1":
        coverage_dir = pathlib.Path(os.getenv("COVERAGE_DIR"))
        coverage_file = coverage_dir / ".coverage"
        coverage_manifest = pathlib.Path(os.getenv("COVERAGE_MANIFEST"))
        coverage_sources = coverage_manifest.read_text().splitlines()
        #print(help(coverage.Coverage))
        #sys.exit(42)
        cov = coverage.Coverage(
            data_file=str(coverage_file),
            include=coverage_sources,
            omit=["*test*", "py_unittest_main.py"],
        )
        cov.start()

    try:
        yield
    finally:
        if os.getenv("COVERAGE", None) == "1":
            cov.stop()
            cov.save()
            coverage_lcov.converter.Converter(
                relative_path=True,
                config_file=False,
                data_file_path=str(coverage_file),
            ).create_lcov(os.getenv("COVERAGE_OUTPUT_FILE"))
