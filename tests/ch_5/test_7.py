import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        ("ULURRDLLU", 7),
        ("LULLLLLLU", 7),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_5
def test_7(module, test_input):
    # given
    dirs, excepted = test_input

    # when
    result = module.solution(dirs)

    # then
    assert result == excepted
