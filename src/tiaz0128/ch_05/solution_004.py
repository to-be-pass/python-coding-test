def solution(answers):
    # 1. 각자의 패턴을 입력
    math_give_up_people = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    # 2. 각자의 패턴으로 문제의 정답과 매칭
    #  - 각자 패턴의 길이가 다른것 확인 -> 돌아가면서 = 묘듈러 연산
    result = [0] * len(math_give_up_people)

    for i, answer in enumerate(answers):
        for j, person in enumerate(math_give_up_people):
            if answer == person[i % len(person)]:
                result[j] = result[j] + 1

    # 3. 그 중에 누가 가장 높은 점수 인지
    #  - 사람의 번호는 1번 부터
    #  - 여럿이면 오름 차순 정렬
    max_correct_cnt = max(result)
    return [
        who for who, correct_cnt in enumerate(result) if correct_cnt == max_correct_cnt
    ]
