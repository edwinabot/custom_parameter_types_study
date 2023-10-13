from enum import Enum

from cucumber_expressions.parameter_type import ParameterType

from .parameter_type_maker_mixin import ParameterTypeMakerMixin


class AirCoolingDeviceTypes(ParameterTypeMakerMixin, Enum):
    AirCoolerFoo = "Air Cooler Foo"
    AirCoolerBar = "Air Cooler Bar"

    @classmethod
    def make_parameter_type(cls) -> ParameterType:
        return ParameterType(
            name="AirCoolingDeviceTypes",
            regexp="Air Cooler Foo|Air Cooler Bar",
            type=cls,
            transformer=lambda s: cls[s.translate(cls.delete_table)],
            use_for_snippets="",
            prefer_for_regexp_match=False,
        )
