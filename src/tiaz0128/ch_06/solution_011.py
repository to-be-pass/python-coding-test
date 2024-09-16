def solution(s):
    # 0. 길이가 1이면 -> 0
    if len(s) < 2:
        return 0

    stack = []

    # 1. 반복해서 문자열 끝가지 가고
    for ch in s:
        # 2. 스택에 값을 넣고
        if not stack:
            stack.append(ch)

        # 3. 하나, 그다음 하나 를 확인 = 같은 경우 pop
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return 1 if not stack else 0
