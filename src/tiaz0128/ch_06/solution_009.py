def solution(decimal):
    stack = []
    mock = decimal
    while True:
        # 2. 나눈 나머지를 스택에 저장한다.
        stack.append(mock % 2)

        # 1. 해당 숫자를 2로 계속 나눈다.
        mock = mock // 2

        # 3. 더이상 나눌수 없으면 반복을 멈춘다.
        if mock < 2:
            stack.append(mock)
            break

    # 4. 스택에 저장한 값을 거꾸로 적는다.
    return "".join(map(str, stack[::-1]))
