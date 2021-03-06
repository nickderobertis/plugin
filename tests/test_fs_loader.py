from plugin import FilePluginLoader
from tests import config as conf

def test_load_and_run_python():
    expect_single_arg = conf.EXPECT_PROJECT_1_PYTHON_META_DICT['on_single_arg']
    loader = FilePluginLoader()
    plugin = loader.load_chain(expect_single_arg)
    assert plugin.on_single_arg(5) == 25