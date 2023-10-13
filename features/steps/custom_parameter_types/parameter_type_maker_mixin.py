from cucumber_expressions.parameter_type import ParameterType


class ParameterTypeMakerMixin:
    # Remove these characters from the parameter names before
    # we create enums from the parameter names.
    delete_dict = {" ": "", "-": ""}
    delete_table = str.maketrans(delete_dict)

    @classmethod
    def make_parameter_type(cls) -> ParameterType:
        """Builds a ParameterType for the current class."""
        raise NotImplementedError
