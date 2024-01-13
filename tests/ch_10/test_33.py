import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (3, [["u", 0, 1], ["u", 1, 2], ["f", 2]], 1),
        (4, [["u", 0, 1], ["u", 2, 3], ["f", 0]], 2),
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
