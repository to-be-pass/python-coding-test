def solution(arr1, arr2):
    # arr2 에서 각 열을 기준으로 계산 대상을 재구성
    arr2_transposed = list(zip(*arr2))

    result = []
    # for arr1 행
    for row in arr1:
        #  for arr2 열
        result.append([sum(a * b for a, b in zip(row, col)) for col in arr2_transposed])

    return result
