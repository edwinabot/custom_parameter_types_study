from typing import List

from behave.matchers import matcher_mapping
from cucumber_expressions.parameter_type import ParameterType
from cucumber_expressions.parameter_type_registry import ParameterTypeRegistry
from cuke4behave.step_matcher import CucumberExpressionMatcher

from features.steps.custom_parameter_types.parameter_type_maker_mixin import (
    ParameterTypeMakerMixin,
)

parameter_type_registry = ParameterTypeRegistry()


def build_step_matcher(func, pattern):
    """Partial constructor."""
    return CucumberExpressionMatcher(
        func, pattern, parameter_type_registry=parameter_type_registry
    )


matcher_mapping["cucumber_expressions"] = build_step_matcher


def register_parameter_types(types: List[ParameterTypeMakerMixin]):
    """Register the parameter types."""
    for parameter_type in types:
        parameter_type_registry.define_parameter_type(
            parameter_type.make_parameter_type()
        )
