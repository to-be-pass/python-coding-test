def solution(N, stages):
    counts = [0 for _ in range(N + 2)]
    accs = [0 for _ in range(N + 3)]
    fail_rate = [0 for _ in range(N + 1)]

    for last_stage in stages:
        counts[last_stage] += 1
    for i in range(N + 1, 0, -1):
        accs[i] = accs[i + 1] + counts[i]
    for i in range(1, N + 1):
        fail_rate[i] = counts[i] / accs[i]
    ret = [i for i in range(1, N + 1)]
    ret.sort(key=lambda x : -fail_rate[x])

    return ret