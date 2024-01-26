def solution(lst : list[int]) -> list[int]:
    '''
    배열의 중복값을 제거하고, 내림차순으로 정렬해서 반환하는 함수
    '''
    used = set()
    unique = [x for x in lst if x not in used and (used.add(x) or True)]
    return sorted(unique, reverse=True)
