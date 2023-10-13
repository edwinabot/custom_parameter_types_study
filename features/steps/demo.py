from typing import Union
from behave import given, when, then

from custom_parameter_types import WaterCoolingDeviceTypes, AirCoolingDeviceTypes


@given("we are using a {WaterCoolingDeviceTypes}")
@given("we are using a {AirCoolingDeviceTypes}")
def use_water_cooling_device(
    context, device: Union[WaterCoolingDeviceTypes, AirCoolingDeviceTypes]
):
    context.water_cooling_device = device


@given("the fluid temperature is {float} degrees")
def set_initial_fluid_temperature(context, temperature: float):
    context.initial_fluid_temperature = temperature


@when("we cool {float} liters of fluid by {float} degrees")
def cool_some_volume_of_fluid(context, volume: float, degrees_to_decrease: float):
    context.final_fluid_temperature = (
        context.initial_fluid_temperature - degrees_to_decrease
    )


@then("the fluid should be {float} degrees")
def step_impl(context, expected_final_temperature: float):
    assert context.final_fluid_temperature == expected_final_temperature
