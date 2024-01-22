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
            ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
            [2, 3, 4],
            ["AC", "ACDE", "BCFG", "CDE"],
        ),
        (
            ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
            [2, 3, 5],
            ["ACD", "AD", "ADE", "CD", "XYZ"],
        ),
        (
            ["XYZ", "XWY", "WXA"],
            [2, 3, 4],
            ["WX", "XY"],
        ),
    ],
)
def setup(request, integrity_module):
    check_integrity(
        DummyRequest(request.param, request.param_index),
        integrity_module.solution,
    )
    return request.param


@pytest.mark.ch_08
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
