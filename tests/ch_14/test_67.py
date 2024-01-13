import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (10, 2, [4, 3]),
        (8, 1, [3, 3]),
        (24, 24, [8, 6]),
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
