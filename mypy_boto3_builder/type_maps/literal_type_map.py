"""
String to type annotation map to replace overriden botocore literals.
"""

from collections.abc import Mapping
from typing import Final

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.utils.lookup_dict import LookupDict

LITERAL_TYPE_MAP: Final[Mapping[ServiceName, Mapping[str, set[str]]]] = {
    # FIXME: https://github.com/boto/botocore/issues/3128
    ServiceNameCatalog.ec2: {"PlatformValuesType": {"windows"}}
}

_LOOKUP: LookupDict[set[str]] = LookupDict(
    {ServiceNameCatalog.to_str(k): v for k, v in LITERAL_TYPE_MAP.items()}
)


def get_type_literal_stub(service_name: ServiceName, literal_name: str) -> TypeLiteral | None:
    """
    Get stub type for botocore literal.

    Arguments:
        service_name -- Service name.
        literal_name -- Target Literal name.

    Returns:
        Literal children or None.
    """
    literal_children = _LOOKUP.get(service_name.name, literal_name)
    if not literal_children:
        return None

    return TypeLiteral(literal_name, literal_children)
