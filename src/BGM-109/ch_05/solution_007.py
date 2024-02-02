# 방향을 받아서 도착지점을 리턴 합니다.
def move_controller(direction, start):
    x = start[0]
    y = start[1]
    # 스위치 쓰고 싶다
    if direction == "U":
        y += 1
    elif direction == "D":
        y -= 1
    elif direction == "R":
        x += 1
    elif direction == "L":
        x -= 1
    # 범위가 벗어난 경우 
    if x > 5 or x < -5:
        return start

    if y > 5 or y < -5:
        return start

    return [x, y]


def solution(dirs):
    position = [0, 0]
    trace = []
    for d in dirs:
        start_at = position
        end_at = move_controller(d, position)
        # 장외 
        if start_at == end_at:
            continue
        tracing = (start_at[0], start_at[1], end_at[0], end_at[1])
        trace.append(tracing)
        position = end_at
    
    return len(set(trace))


print(solution("ULURRDLLU"))
print(solution('LULLLLLLU'))