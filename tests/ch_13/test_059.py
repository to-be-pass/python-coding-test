import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        ([6, 10, 2], "6210"),
        ([3, 30, 34, 5, 9], "9534330"),
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
