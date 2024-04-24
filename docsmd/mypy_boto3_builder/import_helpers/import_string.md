# ImportString

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](./index.md#import-helpers) / ImportString

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_string](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py) module.

## ImportString

[Show source in import_string.py:11](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L11)

Wrapper for Python import strings.

#### Arguments

- `master` - Master module name
- `parts` - Other import parts

#### Examples

```python
import_string = ImportString("my", "name")

str(import_string)
'my.name'

import_string.render()
'my.name'

import_string.parts.append('test')
import_string.render()
'my.name.test'
```

#### Signature

```python
class ImportString:
    def __init__(self, master_name: str, *parts: str) -> None: ...
```

### ImportString().__add__

[Show source in import_string.py:99](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L99)

Create a new import string by adding another import string parts to the end.

#### Signature

```python
def __add__(self: Self, other: Self | str) -> Self: ...
```

### ImportString().__bool__

[Show source in import_string.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L67)

Whether import string is not empty.

#### Signature

```python
def __bool__(self) -> bool: ...
```

### ImportString().__eq__

[Show source in import_string.py:85](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L85)

Whether import strings produce the same render.

#### Signature

```python
def __eq__(self, other: object) -> bool: ...
```

### ImportString().__gt__

[Show source in import_string.py:91](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L91)

Compare import strings for sorting.

Emulates `isort` logic.

#### Signature

```python
def __gt__(self, other: object) -> bool: ...
```

### ImportString().__hash__

[Show source in import_string.py:79](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L79)

Calculate hash value based on all parts.

#### Signature

```python
def __hash__(self) -> int: ...
```

### ImportString().__str__

[Show source in import_string.py:73](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L73)

Render as a part of a valid Python import statement.

#### Signature

```python
def __str__(self) -> str: ...
```

### ImportString.empty

[Show source in import_string.py:49](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L49)

Create an empty ImportString.

#### Signature

```python
@classmethod
def empty(cls: type[Self]) -> Self: ...
```

### ImportString.from_str

[Show source in import_string.py:42](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L42)

Create from string.

#### Signature

```python
@classmethod
def from_str(cls: type[Self], import_string: str) -> Self: ...
```

### ImportString().master_name

[Show source in import_string.py:149](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L149)

Get first import string part or `builtins`.

#### Signature

```python
@property
def master_name(self) -> str: ...
```

### ImportString.parent

[Show source in import_string.py:58](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L58)

Get parent ImportString.

#### Signature

```python
@classmethod
def parent(cls: type[Self]) -> Self: ...
```

### ImportString().render

[Show source in import_string.py:140](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L140)

Render to string.

#### Returns

Ready to use import string.

#### Signature

```python
def render(self) -> str: ...
```

### ImportString().startswith

[Show source in import_string.py:108](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L108)

Check if import string starts with `other`.

#### Examples

```python
ImportString('my', 'name').startswith(ImportString('my'))
True

ImportString('my_module', 'name').startswith(ImportString('my'))
False

ImportString('my', 'name').startswith(ImportString('my, 'name'))
True

ImportString('my', 'name').startswith(ImportString.empty())
True
```

#### Arguments

- `other` - Other import string.

#### Signature

```python
def startswith(self: Self, other: Self) -> bool: ...
```
