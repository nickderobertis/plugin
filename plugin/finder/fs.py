import os
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple, Iterable, Generator, Sequence, Optional, List, Union, Type

from plugin.spec import PluginSpec
from plugin.finder.base import PluginFinder

DEFAULT_SEARCH_PATHS: Tuple[str, ...] = ("plugins",)

@dataclass
class FilePluginMeta:
    file_path: Union[str, Path]

    def __post_init__(self):
        self.file_path = Path(self.file_path).resolve()

    @property
    def extensions(self) -> List[str]:
        return [suff.replace(".", "").casefold() for suff in self.file_path.suffixes]

    @property
    def name(self) -> str:
        return self.file_path.stem

    @property
    def plugin_name(self) -> str:
        return self.file_path.parent.stem

    def extensions_match(self, exts: Sequence[str]) -> bool:
        exts = [ext.replace(".", "").casefold() for ext in exts]
        return all([ext in exts for ext in self.extensions])


class FileSystemFinder(PluginFinder):
    metadata_class = FilePluginMeta

    def __init__(
        self,
        find_names: Optional[Sequence[str]] = None,
        find_exts: Optional[Sequence[str]] = None,
        search_paths: Iterable[str] = DEFAULT_SEARCH_PATHS,
    ):
        self.find_names = find_names
        self.find_exts = find_exts
        self.search_paths = search_paths
        self._validate()

    def _validate(self):
        if self.find_names is None and self.find_exts is None:
            raise ValueError("must pass at least one of find_names or find_exts")

    @classmethod
    def from_spec(cls, spec: Type[PluginSpec], search_paths: Iterable[str] = DEFAULT_SEARCH_PATHS,):
        return cls(find_names=spec._method_names(), search_paths=search_paths)

    def find(self) -> Generator[FilePluginMeta, None, None]:
        found_meta: List[FilePluginMeta] = []
        for sp in self.search_paths:
            for root, _, files in os.walk(sp):
                for file in files:
                    file_path = os.path.join(root, file)
                    meta = FilePluginMeta(file_path)
                    if self.find_names is not None:
                        if meta.name in self.find_names:
                            found_meta.append(meta)
                            yield meta
                    if self.find_exts is not None:
                        if meta.extensions_match(self.find_exts):
                            if meta not in found_meta:
                                found_meta.append(meta)
                                yield meta
