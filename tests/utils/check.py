import pytest
from copy import deepcopy


def check_integrity(request, solution):
    try:
        *args, excepted = request.param
        if excepted != solution(*args):
            raise Exception("Intentional failure")
    except Exception as e:
        print("\n==== 추가한 테스트 케이스가 올바르지 않습니다! ====")
        print(f"{request.param_index + 1} 번째 테스트 케이스를 확인하세요!")
        pytest.skip("테스트")


class DummyRequest:
    def __init__(self, param, index) -> None:
        self.param = deepcopy(param)
        self.param_index = index
