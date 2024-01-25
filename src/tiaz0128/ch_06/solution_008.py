def solution(s):
    stack = []
    for ch in s:
        # 4. 예외적으로 스택에 아무런 값이 경우 입력값 ) 오는 경우는 False
        if len(stack) == 0 and ch == ")":
            return False

        if ch == "(":  # 1. 입력값이 ( 인 경우 스택에 넣고
            stack.append(ch)

        else:  # 2. 입력값이 ) 인 경우는 스택에 꺼낸다.
            stack.pop()

    # 3. 최종적으로 스택에 값이 없으면 True
    return len(stack) == 0
