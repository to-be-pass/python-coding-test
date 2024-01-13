import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        ([[10, 19], [7, 10], [6, 10]], 15, 273.33),
        ([[10, 60], [20, 100], [30, 120]], 50, 240),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_16
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
