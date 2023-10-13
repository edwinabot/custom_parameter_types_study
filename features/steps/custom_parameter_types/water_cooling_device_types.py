from enum import Enum

from cucumber_expressions.parameter_type import ParameterType

from .parameter_type_maker_mixin import ParameterTypeMakerMixin

# Remove these characters from the parameter names before
# we create enums from the parameter names.
delete_dict = {" ": "", "-": ""}
delete_table = str.maketrans(delete_dict)


class WaterCoolingDeviceTypes(ParameterTypeMakerMixin, Enum):
    water_cooler_foo = "Water Cooler Foo"
    water_cooler_bar = "Water Cooler Bar"

    @classmethod
    def make_parameter_type(cls) -> ParameterType:
        return ParameterType(
            name="WaterCoolingDeviceTypes",
            regexp="Water Cooler Foo|Water Cooler Bar",
            type=cls,
            transformer=lambda s: cls[s.translate(delete_table)],
            use_for_snippets="",
            prefer_for_regexp_match=False,
        )
