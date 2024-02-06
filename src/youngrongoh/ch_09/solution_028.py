import math
def solution(N, A, B):
    length = 2**(math.log(N, 2) + 1) - 1
    idx_a = (length - 1) - (N - A)
    idx_b = (length - 1) - (N - B)
    curr_a = idx_a
    curr_b = idx_b
    count = 0
    while curr_a != curr_b:
        curr_a = round((curr_a - 1.5) / 2)
        curr_b = round((curr_b - 1.5) / 2)
        count += 1
        if count == 10:
            break;
    return count
