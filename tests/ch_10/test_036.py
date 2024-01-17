import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (["119", "97674223", "1195524421"], False),
        (["123", "456", "789"], True),
        (["12", "123", "1235", "567", "88"], False),
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
