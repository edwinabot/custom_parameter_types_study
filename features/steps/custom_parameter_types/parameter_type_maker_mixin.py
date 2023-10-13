from abc import ABCMeta, abstractclassmethod

from cucumber_expressions.parameter_type import ParameterType


class ParameterTypeMakerMixin:
    @abstractclassmethod
    def make_parameter_type(cls) -> ParameterType:
        """Builds a ParameterType for the current class."""
        ...
