import pytest

from src.infrastructure.validators import validate_arn


def test_invalid_arn():

    with pytest.raises(ValueError):

        validate_arn("invalid")
