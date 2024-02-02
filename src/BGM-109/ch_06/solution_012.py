def get_time(price, arr):
    time = 0
    if price < min(arr):
        return len(arr)
    for a in arr:
        time += 1
        if price > a:
            return time
    return time

    
# 시간 복잡도 O(N^2)
def solution(prices):
    return [get_time(p, prices[i + 1:]) if i < (len(prices) - 1) else 0 for i, p in enumerate(prices)]

print(solution([1, 2, 3, 2, 3]))
