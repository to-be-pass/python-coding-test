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
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [
                [0, 1],
                [1, 2],
                [1, 4],
                [0, 8],
                [8, 7],
                [9, 10],
                [9, 11],
                [4, 3],
                [6, 5],
                [4, 6],
                [8, 9],
            ],
            5,
        ),
        (
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [
                [0, 1],
                [0, 2],
                [1, 3],
                [1, 4],
                [2, 5],
                [2, 6],
                [3, 7],
                [4, 8],
                [6, 9],
                [9, 10],
            ],
            5,
        ),
    ],
)
def setup(request, integrity_module):
    check_integrity(
        DummyRequest(request.param, request.param_index),
        integrity_module.solution,
    )
    return request.param


@pytest.mark.ch_09
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
