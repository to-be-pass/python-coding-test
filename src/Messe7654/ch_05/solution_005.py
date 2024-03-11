from typing import List

def solution(
    arr1: List[List[int]],
    arr2: List[List[int]]
    ) -> List[List[int]]:
    '''
    :param arr1 (List[List[int]]) : 행렬
    :param arr2 (List[List[int]]) : 행렬
    :output List[List[int]] : 행렬곱 연산의 결과값
    '''
    arr1_shape = (len(arr1), len(arr1[0]))
    arr2_shape = (len(arr2), len(arr2[0]))

    # (U * W) X (W * V) 는 (U * V)의 shape를 갖는 행렬이 된다.
    ret = [[0] * arr2_shape[1] for i in range(arr1_shape[0])]
    
    for r in range(arr1_shape[0]):
        for c in range(arr2_shape[1]):
            for i in range(arr1_shape[1]):
                ret[r][c] += arr1[r][i] * arr2[i][c]           

    return ret