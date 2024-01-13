import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        ([4, 2, 2, 1, 3, 4], [4, 3, 2, 1]),
        ([2, 1, 1, 3, 2, 5, 4], [5, 4, 3, 2, 1]),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_5
def test_2(module, test_input):
    # given
    lst, excepted = test_input

    # when
    result = module.solution(lst)

    # then
    assert result == excepted
