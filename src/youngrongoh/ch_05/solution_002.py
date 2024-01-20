def solution(lst):
    result = list(set(lst))
    result.sort(reverse=True)
    return result
