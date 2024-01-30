import math


def solution(progresses, speeds):
    answer = []

    n = len(progresses)

    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    max_left = days_left[0]
    cnt = 0

    stack = []

    for day in days_left:
        if day <= max_left:
            cnt += 1
        else:
            stack.append(cnt)
            cnt = 1
            max_left = day

    stack.append(cnt)
    return stack
