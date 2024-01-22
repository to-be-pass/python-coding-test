import pytest

import importlib


from tests.utils.check import check_integrity, DummyRequest


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(name="integrity_module")
def setup_integrity(func):
    path = func(__file__, "dremdeveloper")

    return importlib.import_module(name=path)


@pytest.fixture(
    name="test_input",
    params=[
        (
            [[1, 4], [3, 2], [4, 1]],
            [[3, 3], [3, 3]],
            [[15, 15], [15, 15], [15, 15]],
        ),
        (
            [[2, 3, 2], [4, 2, 4], [3, 1, 4]],
            [[5, 4, 3], [2, 4, 1], [3, 1, 1]],
            [[22, 22, 11], [36, 28, 18], [29, 20, 14]],
        ),
    ],
)
def setup(request, integrity_module):
    check_integrity(
        DummyRequest(request.param, request.param_index),
        integrity_module.solution,
    )
    return request.param


@pytest.mark.ch_05
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
