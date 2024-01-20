# 명령어 별 좌표 이동량
movements = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def solution(dirs):
    points = [(0, 0, 0, 0)]
    for dir in dirs:
        (x, y) = points[-1][:2]
        # 현재 위치에 이동량 더하기
        (next_x, next_y) = list(map(lambda a, b : a + b, (x, y), movements[dir]))
        # 경계를 벗어나게 하는 명령어 무시
        if next_x < -5 or next_x > 5 or next_y < -5 or next_y > 5: continue
        points.append((x, y, next_x, next_y))
        points.append((next_x, next_y, x, y))
    # 중복 제거
    dedup = set(points[1:])
    return len(dedup) / 2
