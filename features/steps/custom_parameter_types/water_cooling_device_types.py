from enum import Enum

from cucumber_expressions.parameter_type import ParameterType

from .parameter_type_maker_mixin import ParameterTypeMakerMixin


class WaterCoolingDeviceTypes(ParameterTypeMakerMixin, Enum):
    WaterCoolerFoo = "Water Cooler Foo"
    WaterCoolerBar = "Water Cooler Bar"

    @classmethod
    def make_parameter_type(cls) -> ParameterType:
        return ParameterType(
            name="WaterCoolingDeviceTypes",
            regexp="Water Cooler Foo|Water Cooler Bar",
            type=cls,
            transformer=lambda s: cls[s.translate(cls.delete_table)],
            use_for_snippets="",
            prefer_for_regexp_match=False,
        )
