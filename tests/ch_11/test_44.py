import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3, 4),
        (
            6,
            [
                [1, 2, 1],
                [1, 3, 2],
                [2, 3, 2],
                [3, 4, 3],
                [3, 5, 2],
                [3, 5, 3],
                [5, 6, 1],
            ],
            4,
            4,
        ),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_11
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
