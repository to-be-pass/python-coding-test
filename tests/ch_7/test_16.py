import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        ([93, 30, 55], [1, 30, 5], [2, 1]),
        ([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1], [1, 3, 2]),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_7
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
