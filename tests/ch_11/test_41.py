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
            [[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]],
            0,
            [[0, -2, -4, 3, -6], [None, 2, 4, 1, 0]],
        ),
        ([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]], 0, [-1]),
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
