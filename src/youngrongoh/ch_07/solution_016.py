from collections import deque
def solution(progresses, speeds):
    queue = deque([[progresses[i], speeds[i], i] for i in range(len(progresses))])
    result = []
    front = 0
    rear = len(queue) - 1
    deploy = 0
    while queue:
        item = queue.popleft()
        item[0] += item[1]
        if item[0] >= 100 and item[2] == front:
            front += 1
            deploy += 1
        else:
            queue.append(item)
        if item[2] == rear:
            if deploy > 0:
                result.append(deploy)
            deploy = 0
    return result
