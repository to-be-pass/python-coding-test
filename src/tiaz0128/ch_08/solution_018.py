def solution(arr, k):
    num_2 = {num: num for num in arr}

    for num_1 in arr:
        x = k - num_1
        if num_1 != x and num_2.get(x):
            return True

    return False
