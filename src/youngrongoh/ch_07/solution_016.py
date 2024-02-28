import math
def solution(progresses, speeds):
    n = len(progresses)
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    result = []

    deploy = 0
    deploy_day = days_left[0]
    for i in range(n):
        if deploy_day >= days_left[i]:
            deploy += 1
        else:
            result.append(deploy)
            deploy = 1
            deploy_day = days_left[i]
        if i == n - 1:
            result.append(deploy)
    return result
