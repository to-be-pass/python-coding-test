from typing import List

def solution(answers : List[int]) -> List[int]:
    '''
    INTPU :
        answer(List[int]) := 문제의 정답들의 배열 
    OUTPUT:
        List[int] := 가장 많이 맞춘 사람의 Index를 담은 배열
    '''
    # 수포자들이 찍는 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5,5]
    ]
    length_of_answers = len(answers)
    
    # 각 수포자들이 맞춘 정답의 수를 기록할 배열
    # numbers_of_correct[i]는 (i + 1)번 수포자가 맞춘 정답의 수를 의미함.
    numbers_of_correct = [0 for i in range(3)]

    # 각 수포자들에 대해서 패턴과 정답이 일치하는, 즉 수포자의 정답의 수를 계산
    for i in range(3):
        for j in range(length_of_answers):
            mod = len(patterns[i])
            if answers[j] == patterns[i][j % mod]:
                numbers_of_correct[i] += 1

    # 가장 높은 점수를 받은 수포자의 점수를 기준으로 하여
    # 가장 높은 점수를 받은 수포자들의 번호를 ret(List)에 담음
    max_value = max(numbers_of_correct)
    ret = [(i + 1) for i, v in enumerate(numbers_of_correct) if v == max_value]
    return ret
