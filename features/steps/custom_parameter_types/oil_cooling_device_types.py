from enum import Enum

from cucumber_expressions.parameter_type import ParameterType

from .parameter_type_maker_mixin import ParameterTypeMakerMixin


class OilCoolingDeviceTypes(ParameterTypeMakerMixin, Enum):
    OilCoolerBaz = "Oil Cooler Baz"
    OilCoolerQueseyo = "Oil Cooler Queseyo"

    @classmethod
    def make_parameter_type(cls) -> ParameterType:
        return ParameterType(
            name="OilCoolingDeviceTypes",
            regexp="Oil Cooler Baz|Oil Cooler Queseyo",
            type=cls,
            transformer=lambda s: cls[s.translate(cls.delete_table)],
            use_for_snippets="",
            prefer_for_regexp_match=False,
        )
