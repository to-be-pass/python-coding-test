from collections  import deque

# 1번 번호표를 가진 사람을 기준으로 K번째 사람을 없앱니다.
# • 없앤 사람 다음 사람을 기준으로 하고 다시 K번째 사람을 없앱니다.

def solution(N, K):
    # 큐를 생성합니다. 
    q = deque(list(range(1, N + 1)))

    # 큐가 0이 될때 까지 반복합니다.
    while len(q) > 1:
        # K번째 사람의 앞 순서까지 진행합니다.
        for _ in range(K - 1):
            q.append(q.popleft())
            q.popleft()
        
    return q[0]

   


N = 5
K = 3
print(solution(N, K))  # 5
