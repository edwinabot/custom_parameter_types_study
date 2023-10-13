from typing import Union
from behave import given, when, then, use_step_matcher

from custom_parameter_types import WaterCoolingDeviceTypes, AirCoolingDeviceTypes


use_step_matcher("cucumber_expressions")


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


@then("the fluid should be {float} degrees cooler")
def step_impl(context, degrees_colder: float):
    assert (
        context.initial_fluid_temperature - context.final_fluid_temperature
        == degrees_colder
    )
