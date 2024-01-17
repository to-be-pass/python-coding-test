def solution(N, stages):
    answer = []
    # 스테이지 별로 실패율 구해서

    for stage_number in range(1, N + 1):
        # 성공한 사람 = 현재 스테이지보다 큰 값
        success = len([person for person in stages if stage_number < person])

        # 실패한 사람 = 현재 스테이지랑 같은 값
        fail = len([person for person in stages if stage_number == person])

        # 실패율 = 실패한 사람 / (성공 + 실패)
        try_people = success + fail
        percent = fail / try_people if try_people else 0

        answer.append((stage_number, percent, try_people))

    # 실패율이 높은 순으로 정렬
    # 1. 실패율이 높은값
    # 2. 실패율이 같은 경누 시도한 사람이 많은 경우
    sorted_stages = sorted(answer, key=lambda x: (-x[1], -x[2]))

    return [stage[0] for stage in sorted_stages]
