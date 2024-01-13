import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (10, "1010"),
        (27, "11011"),
        (12345, "11000000111001"),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_6
def test_9(module, test_input):
    # given
    decimal, excepted = test_input

    # when
    result = module.solution(decimal)

    # then
    assert result == excepted
