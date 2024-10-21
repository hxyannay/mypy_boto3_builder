from packaging.version import Version

from mypy_boto3_builder.utils.version import (
    bump_postrelease,
    get_builder_version,
    get_max_build_version,
    get_min_build_version,
    get_release_version,
)


class TestStrings:
    def test_get_builder_version(self) -> None:
        assert Version(get_builder_version())

    def test_get_min_build_version(self) -> None:
        assert get_min_build_version("1.22.36") == "1.22.0"
        assert get_min_build_version("1.22.48.post13") == "1.22.0"
        assert get_min_build_version("1.13.3") == "1.13.0"
        assert get_min_build_version("1.13.2.post56") == "1.13.0"

    def test_get_max_build_version(self) -> None:
        assert get_max_build_version("1.22.36") == "1.23.0"
        assert get_max_build_version("1.22.48.post13") == "1.23.0"
        assert get_max_build_version("1.13.3") == "1.14.0"
        assert get_max_build_version("1.13.2.post56") == "1.14.0"

    def test_bump_postrelease(self) -> None:
        assert bump_postrelease("1.22.36") == "1.22.36.post1"
        assert bump_postrelease("1.22.36.post") == "1.22.36.post1"
        assert bump_postrelease("1.22.36.post0") == "1.22.36.post1"
        assert bump_postrelease("1.22.36.post5") == "1.22.36.post6"

    def test_get_release_version(self) -> None:
        assert get_release_version("1.22.36") == "1.22.36"
        assert get_release_version("1.22.36.post13") == "1.22.36"
        assert get_release_version("1.13.2.post56+dev123") == "1.13.2"
