from collections import deque
def solution(maps):
    h = len(maps)
    w = len(maps[0])
    queue = deque()
    # 시작 위치 찾기
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                queue.append((i, j))
                break
    visited = [[False] * w for _ in range(h)]
    count = 0
    target = 'L'
    found_exit = False
    while queue:
        next = []
        while queue:
            i, j = queue.popleft()
            # 레버 찾으면 출구 찾기 위해 셋업
            if maps[i][j] == target and target == 'L':
                queue.clear()
                queue.append((i, j))
                visited = [[False] * w for _ in range(h)]
                next = []
                target = 'E'
                break
            # 출구 찾으면 루프 종료
            if maps[i][j] == target and target == 'E':
                queue.clear()
                next = []
                found_exit = True
                break
            if visited[i][j]:
                continue
            visited[i][j] = True
            # 인접 노드 중 유효한 노드만 필터링
            adj = [(r, c) for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] if 0 <= r < h and 0 <= c < w and maps[r][c] != 'X']
            next.extend(adj)
        # 유효한 노드가 있으면 count 증가, 큐에 넣기
        if len(next):
            count += 1
            queue.extend(next)
    return count if found_exit else -1
"""
# 추가 테스트 케이스
- maps: ["LOOES", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], answer: 7
- maps: ["LOOOS", "OOOOO", "OOOOO", "XOOOO", "EXOOO"], answer: -1
"""