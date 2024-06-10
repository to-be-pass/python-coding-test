def solution(n):

    dx = [1, 0, 0, -1] # 하, 우, 상, 좌
    dy = [0, 1, -1, 0]

    snail = [[ 0 for _ in range(n)] for _ in range(n)]
    visited = [[ False for _ in range(n)] for _ in range(n)]

    def backTrack(start, dir, cnt):
        if cnt == (n*n) + 1:
            return

        x, y = start[0], start[1]
        nx, ny = 0, 0
        
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[ny][nx]==True: 
            dir+=1
            backTrack([x, y], dir % 4, cnt)
        else:
            snail[ny][nx] = cnt
            visited[ny][nx] = True
            backTrack([nx, ny], dir % 4, cnt+1)

    snail[0][0] = 1
    visited[0][0] = True
    start = [0,0]
        
    backTrack(start, 0, 2)

    return snail
