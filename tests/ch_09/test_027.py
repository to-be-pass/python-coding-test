import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        ([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6], [True, True, True, False]),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [False, False, False, False, False]),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_09
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
