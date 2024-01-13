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
            8,
            2,
            ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"],
            "OOOOXOOO",
        ),
        (
            8,
            2,
            ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"],
            "OOXOXOOO",
        ),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_6
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
