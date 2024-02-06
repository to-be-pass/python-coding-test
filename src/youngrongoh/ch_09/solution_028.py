def solution(N, A, B):
    answer = 0
    a = A
    b = B
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
    return answer
