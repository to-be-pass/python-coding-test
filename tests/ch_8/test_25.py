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
