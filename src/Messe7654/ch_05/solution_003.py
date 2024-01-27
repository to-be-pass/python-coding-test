def solution(numbers : list[int]) -> list[int]:
    '''
    INPUT : 정수 배열 numbers
    OUTPUT: numbers에서 서로 다른 index를 가지는 2개의 수를 뽑아 더해 만들 수 있는
            모든 수를 오름차순으로 정렬한 배열
    '''
    size = len(numbers)
    added = []
    used = set()
    for i in range(size):
        for j in range(i + 1, size):
            added.append(numbers[i] + numbers[j])
    unique = [x for x in added if x not in used and (used.add(x) or True)]
    return sorted(unique)
