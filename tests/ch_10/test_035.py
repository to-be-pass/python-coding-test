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
            3,
            [
                "tank",
                "kick",
                "know",
                "wheel",
                "land",
                "dream",
                "mother",
                "robot",
                "tank",
            ],
            [3, 3],
        ),
        (
            5,
            [
                "hello",
                "observe",
                "effect",
                "take",
                "either",
                "recognize",
                "encourage",
                "ensure",
                "establish",
                "hang",
                "gather",
                "refer",
                "reference",
                "estimate",
                "executive",
            ],
            [0, 0],
        ),
        (
            2,
            ["hello", "one", "even", "never", "now", "world", "draw"],
            [1, 3],
        ),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_10
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
