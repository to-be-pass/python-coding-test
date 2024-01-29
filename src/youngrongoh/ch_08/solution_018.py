def solution(arr, k):
    hash_table = {}
    for n in arr:
        if n < k:
            hash_table[n] = 1

    for n in arr:
        if k - n != n and hash_table.get(k - n):
            return True
    return False
