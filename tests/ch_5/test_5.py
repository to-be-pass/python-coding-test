import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (
            [[1, 4], [3, 2], [4, 1]],
            [[3, 3], [3, 3]],
            [[15, 15], [15, 15], [15, 15]],
        ),
        (
            [[2, 3, 2], [4, 2, 4], [3, 1, 4]],
            [[5, 4, 3], [2, 4, 1], [3, 1, 1]],
            [[22, 22, 11], [36, 28, 18], [29, 20, 14]],
        ),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_5
def test_5(module, test_input):
    # given
    arr1, arr2, excepted = test_input

    # when
    result = module.solution(arr1, arr2)

    # then
    assert result == excepted
