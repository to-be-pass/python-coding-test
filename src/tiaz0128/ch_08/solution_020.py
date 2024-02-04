from collections import Counter


def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]
