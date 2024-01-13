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
            ["banana", "apple", "rice", "pork", "pot"],
            [3, 2, 2, 2, 1],
            [
                "chicken",
                "apple",
                "apple",
                "banana",
                "rice",
                "apple",
                "pork",
                "banana",
                "pork",
                "rice",
                "pot",
                "banana",
                "apple",
                "banana",
            ],
            3,
        ),
        (
            ["apple"],
            [10],
            [
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
            ],
            0,
        ),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_8
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
