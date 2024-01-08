from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any, Iterable

class Section:
    name: str
    @property
    def compressed(self) -> bool: ...
    @property
    def data_size(self) -> int: ...
    @property
    def data_alignment(self) -> int: ...
    def data(self) -> bytes: ...
    def is_null(self) -> bool: ...
    def __getitem__(self, name: str) -> Any: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class NullSection(Section):
    def is_null(self) -> bool: ...

class StringTableSection(Section):
    def get_string(self, offset: int) -> str: ...

class SymbolTableIndexSection(Section):
    symboltable: int
    def get_section_index(self, n: int) -> int: ...

class SymbolTableSection(Section):
    stringtable: StringTableSection
    def num_symbols(self) -> int: ...
    def get_symbol(self, n: int) -> Symbol: ...
    def get_symbol_by_name(self, name: str) -> Iterable[Symbol] | None: ...
    def iter_symbols(self) -> Iterable[Symbol]: ...

class Symbol:
    entry: Mapping[str, Any]
    name: str
    def __init__(self, entry, name: str) -> None: ...
    def __getitem__(self, name: str) -> Any: ...

class SUNWSyminfoTableSection(Section):
    symboltable: StringTableSection
    def num_symbols(self) -> int: ...
    def get_symbol(self, n: int) -> Symbol: ...
    def iter_symbols(self) -> Iterable[Symbol]: ...

class NoteSection(Section):
    def iter_notes(self) -> Iterable[Mapping]: ...

class StabSection(Section):
    def iter_stabs(self) -> Iterable[Any]: ...

class Attribute:
    extra: Incomplete
    def __init__(self, tag) -> None: ...
    @property
    def tag(self): ...

class AttributesSubsubsection(Section):
    stream: Incomplete
    offset: Incomplete
    structs: Incomplete
    attribute: Incomplete
    header: Incomplete
    attr_start: Incomplete
    def __init__(self, stream, structs, offset, attribute) -> None: ...
    def iter_attributes(self, tag: Incomplete | None = None) -> Iterable[Incomplete]: ...
    @property
    def num_attributes(self): ...
    @property
    def attributes(self): ...

class AttributesSubsection(Section):
    stream: Incomplete
    offset: Incomplete
    structs: Incomplete
    subsubsection: Incomplete
    header: Incomplete
    subsubsec_start: Incomplete
    def __init__(self, stream, structs, offset, header, subsubsection) -> None: ...
    def iter_subsubsections(self, scope: Incomplete | None = None) -> Iterable[Incomplete]: ...
    @property
    def num_subsubsections(self): ...
    @property
    def subsubsections(self): ...
    def __getitem__(self, name): ...

class AttributesSection(Section):
    subsection: Incomplete
    subsec_start: Incomplete
    def __init__(self, header, name, elffile, subsection) -> None: ...
    def iter_subsections(self, vendor_name: Incomplete | None = None) -> Iterable[Incomplete]: ...
    @property
    def num_subsections(self): ...
    @property
    def subsections(self): ...

class ARMAttribute(Attribute):
    value: Incomplete
    extra: Incomplete
    def __init__(self, structs, stream) -> None: ...

class ARMAttributesSubsubsection(AttributesSubsubsection):
    def __init__(self, stream, structs, offset) -> None: ...

class ARMAttributesSubsection(AttributesSubsection):
    def __init__(self, stream, structs, offset) -> None: ...

class ARMAttributesSection(AttributesSection):
    def __init__(self, header, name, elffile) -> None: ...

class RISCVAttribute(Attribute):
    value: Incomplete
    extra: Incomplete
    def __init__(self, structs, stream) -> None: ...

class RISCVAttributesSubsubsection(AttributesSubsubsection):
    def __init__(self, stream, structs, offset) -> None: ...

class RISCVAttributesSubsection(AttributesSubsection):
    def __init__(self, stream, structs, offset) -> None: ...

class RISCVAttributesSection(AttributesSection):
    def __init__(self, header, name, elffile) -> None: ...