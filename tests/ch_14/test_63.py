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
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [
                [9, 8, 7],
                [6, 5, 4],
                [3, 2, 1],
            ],
            [
                [30, 84, 138],
                [24, 69, 114],
                [18, 54, 90],
            ],
        ),
        (
            [
                [2, 4, 6],
                [1, 3, 5],
                [7, 8, 9],
            ],
            [
                [9, 1, 2],
                [4, 5, 6],
                [7, 3, 8],
            ],
            [
                [76, 56, 158],
                [40, 31, 74],
                [76, 60, 134],
            ],
        ),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_14
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
