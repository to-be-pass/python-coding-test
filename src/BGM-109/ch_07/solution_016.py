from collections import deque
import math

def day_work(pro, sp):
    return [x + y for x, y in zip(pro, sp)]

def solution(progresses, speeds):
    # 예상 작업 기간 리스트 
    days = [math.ceil((100 - p) / s)for p, s in zip(progresses, speeds)]
    
    # 큐 
    q = deque(days) 
    # 배포 전 완료 데이터를 담는 리스트
    stack = []
    # 결과
    result = []
   
   # 예상 작업 기간 리스트를 전부 확인한다
    while q:
        stack.append(q.popleft())
        # popleft 후에 인덱스 에러가 발생한다.
       # 인덱스 에러 때문에 브레이크문을 넣어준다.
        if len(q) == 0:
            result.append(len(stack))
            break
        elif stack[-1] < q[0]:
            result.append(len(stack))
            stack = []
        else:
            continue

    return result


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))
# 작업 개수(progresses, speeds의 배열 길이)는 100개 이하입니다.
# • 작업 진도는 100 미만의 자연수입니다.
# • 작업 속도는 100 이하의 자연수입니다.
# • 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도
# 율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.