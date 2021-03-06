from unittest.mock import patch

from plugin import FilePluginLoader
from tests import config as conf
from tests.input_files.project_1.spec import MyChainPlugin, MyAggregatePlugin


def test_load_and_run_python_chain():
    loader = FilePluginLoader()
    plugin_class = MyChainPlugin
    plug = MyChainPlugin()

    expect_single_arg = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_single_arg"]
    plugin = loader.load(expect_single_arg)
    with plugin_class.register(plugin):
        assert plug.on_single_arg(5) == 25

    expect_two_args = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_two_args"]
    plugin = loader.load(expect_two_args)
    with plugin_class.register(plugin):
        assert plug.on_two_args(5, 10) == (25, 30)

    expect_nothing = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_nothing"]
    with patch("plugin.loader.fs.run_file") as mock:
        plugin = loader.load(expect_nothing)
        with plugin_class.register(plugin):
            plug.on_nothing()
            mock.assert_called_once_with(
                loader.file_executors["py"], expect_nothing.file_path
            )

    expect_kwargs = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_kwargs"]
    plugin = loader.load(expect_kwargs)
    with plugin_class.register(plugin):
        assert plug.on_kwargs(value=5) == dict(value=25)

    expect_args_and_kwargs = conf.EXPECT_PROJECT_1_PYTHON_META_DICT[
        "on_args_and_kwargs"
    ]
    plugin = loader.load(expect_args_and_kwargs)
    with plugin_class.register(plugin):
        assert plug.on_args_and_kwargs(5, value2=10) == (25, dict(value2=30))


def test_load_and_run_python_aggregate():
    loader = FilePluginLoader()
    plugin_class = MyAggregatePlugin
    plug = MyAggregatePlugin()

    expect_single_arg = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_single_arg"]
    plugin = loader.load(expect_single_arg)
    with plugin_class.register(plugin):
        assert plug.on_single_arg(5) == [25]

    expect_two_args = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_two_args"]
    plugin = loader.load(expect_two_args)
    with plugin_class.register(plugin):
        assert plug.on_two_args(5, 10) == [(25, 30)]

    expect_nothing = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_nothing"]
    with patch("plugin.loader.fs.run_file") as mock:
        plugin = loader.load(expect_nothing)
        with plugin_class.register(plugin):
            plug.on_nothing()
            mock.assert_called_once_with(
                loader.file_executors["py"], expect_nothing.file_path
            )

    expect_kwargs = conf.EXPECT_PROJECT_1_PYTHON_META_DICT["on_kwargs"]
    plugin = loader.load(expect_kwargs)
    with plugin_class.register(plugin):
        assert plug.on_kwargs(value=5) == [dict(value=25)]

    expect_args_and_kwargs = conf.EXPECT_PROJECT_1_PYTHON_META_DICT[
        "on_args_and_kwargs"
    ]
    plugin = loader.load(expect_args_and_kwargs)
    with plugin_class.register(plugin):
        assert plug.on_args_and_kwargs(5, value2=10) == [(25, dict(value2=30))]
