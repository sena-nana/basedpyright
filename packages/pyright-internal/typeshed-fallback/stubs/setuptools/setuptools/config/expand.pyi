from _typeshed import Incomplete, StrPath
from collections.abc import Callable, Iterable, Iterator, Mapping
from importlib.machinery import ModuleSpec
from types import TracebackType
from typing import TypeVar
from typing_extensions import Self

from ..dist import Distribution

_K = TypeVar("_K")
_VCo = TypeVar("_VCo", covariant=True)

class StaticModule:
    def __init__(self, name: str, spec: ModuleSpec) -> None: ...
    def __getattr__(self, attr): ...

def glob_relative(patterns: Iterable[str], root_dir: StrPath | None = None) -> list[str]: ...
def read_files(filepaths: StrPath | Iterable[StrPath], root_dir: StrPath | None = None) -> str: ...
def read_attr(attr_desc: str, package_dir: Mapping[str, str] | None = None, root_dir: StrPath | None = None): ...
def resolve_class(
    qualified_class_name: str, package_dir: Mapping[str, str] | None = None, root_dir: StrPath | None = None
) -> Callable[..., Incomplete]: ...
def cmdclass(
    values: dict[str, str], package_dir: Mapping[str, str] | None = None, root_dir: StrPath | None = None
) -> dict[str, Callable[..., Incomplete]]: ...
def find_packages(
    *, namespaces: bool = True, fill_package_dir: dict[str, str] | None = None, root_dir: StrPath | None = None, **kwargs
) -> list[str]: ...
def version(value: Callable[..., Incomplete] | Iterable[str | int] | str) -> str: ...
def canonic_package_data(package_data: dict[Incomplete, Incomplete]) -> dict[Incomplete, Incomplete]: ...
def canonic_data_files(
    data_files: list[Incomplete] | dict[Incomplete, Incomplete], root_dir: StrPath | None = None
) -> list[tuple[str, list[str]]]: ...
def entry_points(text: str, text_source: str = "entry-points") -> dict[str, dict[Incomplete, Incomplete]]: ...

class EnsurePackagesDiscovered:
    def __init__(self, distribution: Distribution) -> None: ...
    def __call__(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, _exc_type: type[BaseException] | None, _exc_value: BaseException | None, _traceback: TracebackType | None
    ) -> None: ...
    @property
    def package_dir(self) -> Mapping[str, str]: ...

class LazyMappingProxy(Mapping[_K, _VCo]):
    def __init__(self, obtain_mapping_value: Callable[[], Mapping[_K, _VCo]]) -> None: ...
    def __getitem__(self, key: _K) -> _VCo: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
