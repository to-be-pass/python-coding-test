from collections import deque


def solution(progresses, speeds):
    pq = deque(zip(progresses, speeds))
    stack = []

    while pq:
        for idx, (pro, speed) in enumerate(pq):
            pq[idx] = (pro + speed, speed)

        cnt = 0
        for item in pq:
            if item[0] >= 100:
                cnt += 1
            else:
                break

        if cnt > 0:
            for _ in range(cnt):
                pq.popleft()

            stack.append(cnt)

    return stack
