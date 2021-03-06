from abc import ABC, abstractmethod
from typing import List, Any, Tuple, Dict, Optional

from plugin.spec import PluginSpec


class Plugin(ABC):
    handlers: List[PluginSpec] = []

    @classmethod
    def register(cls, plugin: PluginSpec):
        cls.handlers.append(plugin)

    @classmethod
    def deregister(cls, plugin: PluginSpec):
        cls.handlers.remove(plugin)

    @abstractmethod
    def execute(self, method_name: str, *args, **kwargs):
        ...
