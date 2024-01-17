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
            {"A": {"B": 9, "C": 3}, "B": {"A": 5}, "C": {"B": 1}},
            "A",
            [
                {"A": 0, "B": 4, "C": 3},
                {"A": ["A"], "B": ["A", "C", "B"], "C": ["A", "C"]},
            ],
        ),
        (
            {"A": {"B": 1}, "B": {"C": 5}, "C": {"D": 1}, "D": {}},
            "A",
            [
                {"A": 0, "B": 1, "C": 6, "D": 7},
                {
                    "A": ["A"],
                    "B": ["A", "B"],
                    "C": ["A", "B", "C"],
                    "D": ["A", "B", "C", "D"],
                },
            ],
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
