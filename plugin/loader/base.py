from typing import Generator, TypeVar, Type, List, Sequence, Iterable
from typing_extensions import Protocol

from plugin import ChainPlugin, AggregatePlugin

T = TypeVar("T")


class PluginLoader(Protocol[T]):
    metadata_class: Type[T]

    def load_chain(self, meta: T) -> ChainPlugin:
        ...

    def load_chain_all(self, metas: Iterable[T]) -> List[ChainPlugin]:
        return [self.load_chain(meta) for meta in metas]

    def load_aggregate(self, meta: T) -> AggregatePlugin:
        ...

    def load_aggregate_all(self, metas: Iterable[T]) -> List[AggregatePlugin]:
        return [self.load_aggregate(meta) for meta in metas]
