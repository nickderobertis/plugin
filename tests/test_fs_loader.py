from unittest.mock import patch

from plugin import FilePluginLoader
from tests import config as conf


def test_load_and_run_python():
    loader = FilePluginLoader()

    expect_single_arg = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_single_arg"]
    plugin = loader.load_chain(expect_single_arg)
    assert plugin.on_single_arg(5) == 25

    expect_two_args = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_two_args"]
    plugin = loader.load_chain(expect_two_args)
    assert plugin.on_two_args(5, 10) == (25, 30)

    expect_nothing = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_nothing"]
    with patch('plugin.loader.fs.run_file') as mock:
        plugin = loader.load_chain(expect_nothing)
        plugin.on_nothing()
        mock.assert_called_once_with(loader.file_executors['py'], expect_nothing.file_path)

    expect_kwargs = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_kwargs"]
    plugin = loader.load_chain(expect_kwargs)
    assert plugin.on_kwargs(value=5) == dict(value=25)

    expect_args_and_kwargs = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_args_and_kwargs"]
    plugin = loader.load_chain(expect_args_and_kwargs)
    assert plugin.on_args_and_kwargs(5, value2=10) == (25, dict(value2=30))
