import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (1, False),
        (2, False),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_12
def test_8(module, test_input):
    # given
    num, excepted = test_input

    # when
    result = module.solution()

    # then
    assert result == excepted
