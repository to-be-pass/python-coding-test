def solution(participant, completion):
    a = {part: 0 for part in participant}
    for x in participant:
        a[x] += 1

    for x in completion:
        a[x] -= 1

    return [x for x in a if a[x] != 0][0]
