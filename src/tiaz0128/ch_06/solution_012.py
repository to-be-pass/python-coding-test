def solution(prices):
    # O(N^2)
    length = len(prices)
    answer = [0] * length

    stack = []
    for idx, prev_price in enumerate(prices):
        if idx == length - 1:
            stack.append(idx)
            break

        next_price = prices[idx + 1]

        # 1. 주식 가격이 떨어지지 않으면 계속 스택에 인덱스값을 저장한다.
        if prev_price <= next_price:
            stack.append(idx)
        # 2. 주식 가격이 떨어지면 스택에 저장되어 있는 인덱스의 값들을 확인하고
        else:
            stack.append(idx)
            while True:
                # 3. 떨어지는 값보다 인덱스에 있는 값이 더 큰 경우
                if stack and prices[stack[-1]] > next_price:
                    # 4. 답을 입력하고 POP
                    target_idx = stack.pop()
                    answer[target_idx] = idx - target_idx + 1
                else:
                    break

    # 5. 마지막까지 남아 있는값들은 len(prices) - index값 - 1
    for idx in stack:
        answer[idx] = length - idx - 1

    return answer
