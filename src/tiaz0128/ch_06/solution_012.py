def solution(prices):
    answer = []
    # 1. prices 를 반복하면서 기준이 되는 start 를 하나씩 증가
    for idx, price in enumerate(prices, 1):
        # 2. start 에서 그 이후에 있는 값들과 비교
        cnt = 0
        for compare_price in prices[idx:]:
            # 4. 단, 바로 다음에 떨어지더라도 1초로 시작 = 기록하는 값은 1초로 시작
            cnt += 1
            # 3. 비교는 기준 start 보다 비교값이 더 작은경우에
            if compare_price >= price:
                continue
            else:
                break
        answer.append(cnt)

    return answer
