def solution(prices):
    n = len(prices)
    result = [0] * n  # 결과 배열 초기화

    stack = []  # 인덱스를 저장할 스택

    for i in range(n):
        
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
        
    while stack:
        j = stack.pop()
        result[j] = n - 1 - j

    return result

print(solution([1, 2, 3, 2, 3]))