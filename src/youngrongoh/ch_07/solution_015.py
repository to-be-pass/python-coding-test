def solution(N, K):
    queue = [i for i in range(N)]
    idx = 0
    while len(queue) > 1:
        idx = (idx + K - 1) % len(queue)
        queue.pop(idx)
    return queue.pop() + 1
