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
            [["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"]],
            "A",
            ["A", "B", "C", "D", "E"],
        ),
        (
            [["A", "B"], ["A", "C"], ["B", "D"], ["B", "E"], ["C", "F"], ["E", "F"]],
            "A",
            ["A", "B", "D", "E", "F", "C"],
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
