import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        ([1, -5, 2, 4, 3], [-5, 1, 2, 4, 3]),
        ([2, 1, 1, 3, 2, 5, 4], [1, 1, 2, 2, 3, 4, 5]),
        ([6, 1, 7], [1, 6, 7]),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_5
def test_1(module, test_input):
    # given
    arr, excepted = test_input

    # when
    result = module.solution(arr)

    # then
    assert result == excepted
