from collections import deque
def solution(progresses, speeds):
    queue = deque([[progresses[i], speeds[i]] for i in range(len(progresses))])
    result = []
    while queue:
        for i in range(len(queue)):
            queue[i][0] += queue[i][1]
        deploy = 0
        while queue and queue[0][0] >= 100:
            deploy += 1
            queue.popleft()
        if deploy > 0:
            result.append(deploy)
    return result
