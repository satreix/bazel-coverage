load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_bats",
    sha256 = "1a4827bb6b9ed8a306061b74af9d7b9c23e029cd85e33e4338b4c97934b0d0ec",
    strip_prefix = "bazel-bats-43ca3e224edd5f5728a454ec2937c8c489998d7e",
    urls = ["https://github.com/filmil/bazel-bats/archive/43ca3e224edd5f5728a454ec2937c8c489998d7e.tar.gz"],
)

http_archive(
    name = "bazel_gazelle",
    sha256 = "de69a09dc70417580aabf20a28619bb3ef60d038470c7cf8442fafcf627c21cb",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.24.0/bazel-gazelle-v0.24.0.tar.gz",
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.24.0/bazel-gazelle-v0.24.0.tar.gz",
    ],
)

http_archive(
    name = "contrib_rules_jvm",
    sha256 = "4242ed2e537efb0770989bac5b4db849091b67b905193c4a0b096398013e25fd",
    strip_prefix = "rules_jvm-661d1eea3f1e4a4dd457b57dfd23dd6d46e15205",
    urls = ["https://github.com/bazel-contrib/rules_jvm/archive/661d1eea3f1e4a4dd457b57dfd23dd6d46e15205.tar.gz"],
)

http_archive(
    name = "gtest",
    sha256 = "b4870bf121ff7795ba20d20bcdd8627b8e088f2d1dab299a031c1034eddc93d5",
    strip_prefix = "googletest-release-1.11.0",
    urls = ["https://github.com/google/googletest/archive/release-1.11.0.tar.gz"],
)

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "2b1641428dff9018f9e85c0384f03ec6c10660d935b750e3fa1492a281a53b0f",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.29.0/rules_go-v0.29.0.zip",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.29.0/rules_go-v0.29.0.zip",
    ],
)

http_archive(
    name = "rules_cc",
    sha256 = "935e2644125fccb36fa858495697301f7834d980d0e16419943b9618af2771a4",
    strip_prefix = "rules_cc-0.0.1",
    urls = ["https://github.com/bazelbuild/rules_cc/archive/0.0.1.tar.gz"],
)

http_archive(
    name = "rules_java",
    sha256 = "ddc9e11f4836265fea905d2845ac1d04ebad12a255f791ef7fd648d1d2215a5b",
    strip_prefix = "rules_java-5.0.0",
    urls = ["https://github.com/bazelbuild/rules_java/archive/5.0.0.tar.gz"],
)

http_archive(
    name = "rules_jvm_external",
    sha256 = "cd1a77b7b02e8e008439ca76fd34f5b07aecb8c752961f9640dea15e9e5ba1ca",
    strip_prefix = "rules_jvm_external-4.2",
    url = "https://github.com/bazelbuild/rules_jvm_external/archive/4.2.zip",
)

http_archive(
    name = "rules_python",
    sha256 = "a2fd4c2a8bcf897b718e5643040b03d9528ac6179f6990774b7c19b2dc6cd96b",
    strip_prefix = "rules_python-0.5.0",
    urls = ["https://github.com/bazelbuild/rules_python/archive/0.5.0.tar.gz"],
)

load("@contrib_rules_jvm//:repositories.bzl", "contrib_rules_jvm_deps")

contrib_rules_jvm_deps()

load("@contrib_rules_jvm//:setup.bzl", "contrib_rules_jvm_setup")

contrib_rules_jvm_setup()

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains(version = "1.17.2")

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")

gazelle_dependencies()

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "pypi",
    requirements = "//third_party/python:requirements.txt",
)

load("@rules_jvm_external//:defs.bzl", "maven_install")

maven_install(
    artifacts = [
        "org.junit.jupiter:junit-jupiter-api:5.8.2",
        "org.junit.jupiter:junit-jupiter-engine:5.8.2",
        "org.junit.jupiter:junit-jupiter:5.8.2",
        "org.junit.platform:junit-platform-launcher:1.8.2",
        "org.junit.platform:junit-platform-reporting:1.8.2",
    ],
    fetch_sources = True,
    repositories = [
        "https://repo1.maven.org/maven2",
    ],
)

load("@bazel_bats//:deps.bzl", "bazel_bats_dependencies")

bazel_bats_dependencies()
