from collections import deque

def solution(N, K):
    queue = deque([i + 1 for i in range(N)])
    while len(queue) > 1:
        for _ in range(K - 1):
          queue.append(queue.popleft())
        queue.popleft()
    return queue.popleft()
