def solution(numbers):
    unique_sum = set([])
    for i, n in enumerate(numbers):
        for m in numbers[i+1:]:
            unique_sum.add(n + m)
    result = list(unique_sum)
    result.sort()
    return result
