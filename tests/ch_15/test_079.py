import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (["ba", "na", "n", "a"], "banana", 3),
        (["app", "ap", "p", "l", "e", "ple", "pp"], "apple", 2),
        (["ba", "an", "nan", "ban", "n"], "banana", -1),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_15
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
