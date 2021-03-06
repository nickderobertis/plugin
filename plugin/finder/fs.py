import os
from pathlib import Path
from typing import Tuple, Iterable, Generator, Sequence, Optional, List, Union

from plugin.finder.base import PluginFinder

DEFAULT_SEARCH_PATHS: Tuple[str, ...] = ("plugins",)


class FilePluginMeta:
    def __init__(self, file_path: Union[str, Path]):
        self.file_path = Path(file_path)

    @property
    def extensions(self) -> List[str]:
        return [suff.replace(".", "").casefold() for suff in self.file_path.suffixes]

    @property
    def name(self) -> str:
        return self.file_path.stem

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

    def find(self) -> Generator[FilePluginMeta, None, None]:
        found_meta: List[FilePluginMeta] = []
        for sp in self.search_paths:
            for file in next(os.walk(sp))[2]:
                meta = FilePluginMeta(file)
                if self.find_names is not None:
                    if meta.name in self.find_names:
                        found_meta.append(meta)
                        yield meta
                if self.find_exts is not None:
                    if meta.extensions_match(self.find_exts):
                        if meta not in found_meta:
                            found_meta.append(meta)
                            yield meta
