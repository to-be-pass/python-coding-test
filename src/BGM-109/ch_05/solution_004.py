# requirements 
# answer 는 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

# 학생들의 점수를 출력하는 함수
# 시간 복잡도 O(n)
def grade(answer, pattern):
    grade = 0
    n = len(pattern)
    for i, a in enumerate(answer):
        if a == pattern[(i % n)]:
            grade += 1
    return grade;

def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    students = [s1, s2, s3]
    # 학생들의 점수
    grades = [grade(answers, s) for s in students]
    # 최고 득점
    max_g = max(grades)
    # 결과 
    result = []
    for i, g in enumerate(grades):
        if g == max_g:
            result.append(i + 1)
    return result


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))