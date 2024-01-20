def solution(numbers):
    # 순회하면 더하기 : O(N2)
    answer = []
    for i, num1 in enumerate(numbers):
        for num2 in numbers[i + 1 :]:
            answer.append(num1 + num2)

    # 중복 제거 : O(N)
    # 정렬 : O(NlogN)
    return sorted(set(answer))
