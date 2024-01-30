def solution(participant, completion):
    hash_table = {}
    for c in completion:
        if c in hash_table:
            hash_table[c] += 1
        else:
            hash_table[c] = 1

    answer = ''
    for p in participant:
        if p in hash_table and hash_table[p] > 0:
            hash_table[p] -= 1
        else:
            answer = p
            break;

    return answer
