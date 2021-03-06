from typing import Generator, TypeVar, Type, List, Sequence, Iterable
from typing_extensions import Protocol

from plugin import ChainPlugin, AggregatePlugin, PluginSpec

T = TypeVar("T")


class PluginLoader(Protocol[T]):
    metadata_class: Type[T]

    def load(self, meta: T) -> PluginSpec:
        ...

    def load_all(self, metas: Iterable[T]) -> List[PluginSpec]:
        return [self.load(meta) for meta in metas]
