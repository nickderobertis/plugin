from typing import Any, List

from plugin import FileSystemFinder
from plugin.finder.fs import FilePluginMeta
from tests import config as conf
from tests.input_files.project_1.spec import MyPluginSpec

EXPECT_METAS: List[FilePluginMeta] = [
    FilePluginMeta(conf.PROJECT_1_FS_PLUG_PATH / "on_nothing.py"),
    FilePluginMeta(conf.PROJECT_1_FS_PLUG_PATH / "on_args_and_kwargs.py"),
    FilePluginMeta(conf.PROJECT_1_FS_PLUG_PATH / "on_kwargs.py"),
    FilePluginMeta(conf.PROJECT_1_FS_PLUG_PATH / "on_single_arg.py"),
    FilePluginMeta(conf.PROJECT_1_FS_PLUG_PATH / "on_two_args.py"),
]
EXPECT_METAS.sort(key=lambda meta: meta.name)


def _assert_found(finder: FileSystemFinder, found: Any):
    find_iter: List[FilePluginMeta] = [item for item in finder.find()]
    find_iter.sort(key=lambda meta: meta.name)
    assert find_iter == found
    assert sorted(finder.find_all(), key=lambda meta: meta.name) == found


def test_fs_finder_find_names():
    finder = FileSystemFinder(
        ["on_nothing"], search_paths=[conf.PROJECT_1_FS_PLUG_PATH]
    )
    expect_meta = FilePluginMeta(conf.PROJECT_1_FS_PLUG_PATH / "on_nothing.py")
    _assert_found(finder, [expect_meta])


def test_fs_finder_find_exts():
    finder = FileSystemFinder(
        find_exts=["py"], search_paths=[conf.PROJECT_1_FS_PLUG_PATH]
    )
    _assert_found(finder, EXPECT_METAS)


def test_fs_finder_from_spec():
    finder = FileSystemFinder.from_spec(
        MyPluginSpec, search_paths=[conf.PROJECT_1_FS_PLUG_PATH]
    )
    _assert_found(finder, EXPECT_METAS)
