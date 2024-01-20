def solution(lst):
    # 1. 배열의 중복값 제거 = set
    unique_lst = list(set(lst))
    # 2. 내림차순 정렬 = sorted
    return sorted(unique_lst, reverse=True)
