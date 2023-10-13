from behave import use_step_matcher
from .custom_parameter_type_registrar import register_parameter_types

from .air_cooling_device_types import AirCoolingDeviceTypes
from .water_cooling_device_types import WaterCoolingDeviceTypes
from .oil_cooling_device_types import OilCoolingDeviceTypes

register_parameter_types(
    [WaterCoolingDeviceTypes, AirCoolingDeviceTypes, OilCoolingDeviceTypes]
)
use_step_matcher("cucumber_expressions")
