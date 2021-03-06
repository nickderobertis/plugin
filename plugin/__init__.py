"""
A flexible Python plugin framework supporting plugins in multiple languages
"""
from plugin.spec import PluginSpec
from plugin.plugin import Plugin
from plugin.chain_plugin import ChainPlugin
from plugin.aggregate_plugin import AggregatePlugin
from plugin.finder.fs import FileSystemFinder
from plugin.loader.fs import FilePluginLoader