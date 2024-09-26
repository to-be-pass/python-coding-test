# n = 표의 행 개수
# k = 처음 선택된 행의 위치
# cmd = 수행한 명령어 문자배열


def solution(n, k, cmd):
    dirs = {"U": -1, "D": 1}
    stack = []

    arr = ["O"] * n

    for command in cmd:
        print(f"k = {k} / command {command}")

        if command == "C":
            stack.append(k)
            arr.pop(k)

            if k == len(arr):
                k -= 1
            pass
        elif command == "Z":
            idx = stack.pop()

            if idx <= k:
                k += 1

            arr.insert(idx, "O")
            pass
        else:
            dir, cnt = command.split(" ")
            k += dirs[dir] * int(cnt)

        print("k=", k)

    for idx in reversed(stack):
        arr.insert(idx, "X")

    return "".join(arr)
