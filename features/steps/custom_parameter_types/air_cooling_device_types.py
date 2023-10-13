from enum import Enum

from cucumber_expressions.parameter_type import ParameterType

from .parameter_type_maker_mixin import ParameterTypeMakerMixin

# Remove these characters from the parameter names before
# we create enums from the parameter names.
delete_dict = {" ": "", "-": ""}
delete_table = str.maketrans(delete_dict)


class AirCoolingDeviceTypes(ParameterTypeMakerMixin, Enum):
    air_cooler_foo = "Air Cooler Foo"
    air_cooler_bar = "Air Cooler Bar"

    @classmethod
    def make_parameter_type(cls) -> ParameterType:
        return ParameterType(
            name="AirCoolingDeviceTypes",
            regexp="Air Cooler Foo|Air Cooler Bar",
            type=cls,
            transformer=lambda s: cls[s.translate(delete_table)],
            use_for_snippets="",
            prefer_for_regexp_match=False,
        )
