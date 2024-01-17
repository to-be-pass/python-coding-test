def solution(dirs):
    pass_to_paths = set()

    # 1. 캐릭터는 0, 0 에서 시작한다.
    character = {"x": 0, "y": 0}

    moving_x = {"R": 1, "L": -1}
    moving_y = {"U": 1, "D": -1}

    # 2. dirs 의 명령어의 방향에 따라서 움직인다
    for direction in dirs:
        move_to_x = character["x"] + moving_x.get(direction, 0)
        move_to_y = character["y"] + moving_y.get(direction, 0)

        # 3. 범위를 벗어나는 명령어는 무시
        if (abs(move_to_x) > 5) or (abs(move_to_y) > 5):
            continue
        pass_to_paths.add((character["x"], character["y"], move_to_x, move_to_y))
        pass_to_paths.add((move_to_x, move_to_y, character["x"], character["y"]))

        character["x"] = move_to_x
        character["y"] = move_to_y

    # 4. 지나간 길들 중에서 유니크한 값만 뽑아 낸다.
    return len(pass_to_paths) / 2
