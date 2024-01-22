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
            ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
            ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
            ["young", "john", "tod", "emily", "mary"],
            [12, 4, 2, 5, 10],
            [360, 958, 108, 0, 450, 18, 180, 1080],
        ),
        (
            ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
            ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
            ["sam", "emily", "jaimie", "edward"],
            [2, 3, 5, 4],
            [0, 110, 378, 180, 270, 450, 0, 0],
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
