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
                (1, 2),
                (1, 3),
                (2, 4),
                (2, 5),
                (3, 6),
                (3, 7),
                (4, 8),
                (5, 8),
                (6, 9),
                (7, 9),
            ],
            1,
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ),
        (
            [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)],
            1,
            [1, 2, 3, 4, 5, 0],
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
