def solution(N, stages):
    # 각 스테이지에 멈춰 있는 사용자 수 추출
    users = [0] * (N + 1)
    for level in stages:
        users[level - 1] += 1
    # 각 스테이지 별 실패율 계산
    failures = [ None ] * (N + 1)
    acc = 0
    for i in range(N, -1, -1):
        curr = users[i]
        acc += curr
        failure = curr / acc if acc != 0 else 0
        failures[i] = [failure, i + 1]
    # 실패율이 높은 스테이지부터 내림차순으로 정렬
    sorted_failures = sorted(failures[0:-1], key=lambda x : x[0], reverse=True)
    sorted_levels = [x[1] for x in sorted_failures]
    return sorted_levels
