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
            ["classic", "pop", "classic", "classic", "pop"],
            [500, 600, 150, 800, 2500],
            [4, 1, 3, 0],
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
