def solution(s):
    # 추가 테스트 케이스
    # s = '{'
    # s = '}'
    length = len(s)
    if length == 1:
        return 0

    bracket_pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    # 괄호 회전하면서 = 길이 - 1 만큼 회전?
    cnt = 0
    for start in range(length):
        stack = []
        for idx in range(length):
            # print(s[(start + idx) % length], end="")
            ch = s[(start + idx) % length]

            # 1. ( { [ , 여는 문자열은 push
            if ch in ("(", "{", "["):
                stack.append(ch)
            # 2. ) } ] , 닫는 문자열은 pop
            else:
                if not stack or stack[-1] != bracket_pairs.get(ch):
                    break
                stack.pop()

        # 올바른 경우에 카운트 +1
        if not stack and idx == length - 1:
            cnt += 1

    return cnt
