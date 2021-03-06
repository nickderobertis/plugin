from abc import ABC
from typing import Generator, TypeVar, Type, List

T = TypeVar('T')


class PluginMeta:
    pass


class PluginFinder(ABC):
    metadata_class: Type[T]

    def find(self) -> Generator[T, None, None]:
        ...

    def find_all(self) -> List[T]:
        return [item for item in self.find()]