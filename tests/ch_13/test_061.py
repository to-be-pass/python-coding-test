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
                [1, 4, 8, 10],
                [5, 5, 5, 5],
                [10, 10, 10, 10],
                [10, 10, 10, 20],
            ],
            3,
            15,
        ),
        (
            [
                [10, 11, 10, 11],
                [2, 21, 20, 10],
                [1, 20, 21, 11],
                [2, 1, 2, 1],
            ],
            1,
            18,
        ),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_13
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
