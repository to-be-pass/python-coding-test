import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]], 3),
        (4, [[1, 2], [2, 3], [3, 4]], 0),
        (7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]], 1),
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
