#!/bin/bash
set -euo pipefail

COVERAGE_DIR="$(bazel info output_path)/_coverage"

bazel coverage --instrumentation_filter="^//bash[/:],^//cpp[/:],^//go[/:],^//java[/:],^//python[/:],-Test" //...

genhtml --output "${COVERAGE_DIR}/genhtml" "${COVERAGE_DIR}/_coverage_report.dat"
open "${COVERAGE_DIR}/genhtml/index.html"
