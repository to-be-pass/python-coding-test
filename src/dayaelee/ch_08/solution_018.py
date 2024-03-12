def solution(arr, k):

    for i in range (len(arr)):
        for j in range(i, len(arr)):
            if i==j:
                continue
            if arr[i] + arr[j] == k:
                return True
            else:
                continue

    return False
