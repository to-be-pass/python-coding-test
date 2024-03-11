def solution(s : str) -> int:
    """괄호문자열 s를 입력받아 s를 왼쪽으로 x (0 <= x < len(s)) 회전 시켰을 때,
    s가 올바른 괄호 문자열이 되게 하는 x의 개수를 반환하는 함수

    Args:
      s(str) : 괄호 문자열
    Returns:
      s를 왼쪽으로 x (0 <= x < len(s)) 회전 시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수
    """
    def isProper(s : str, shift : int) -> bool:
        """s를 왼쪽으로 shift만큼 회전시킨 문자열이 올바른 괄호문자열인지 판단하는 함수
        
        Args:
          s (str) : 괄호 문자열
          shift (int) : 왼쪽으로 회전 시킬 횟수
        Returns:
          s를 왼쪽으로 shift만큼 rotate 시킨 문자열이 올바른 괄호 문자열인지 여부
        """
        length = len(s)
        stack = []
        for idx in range(length):
            now = s[(idx + shift) % length]
            if now == "[" or now == "{" or now == "(":
                stack.append(now)
            else:
                if not stack:
                    return False
                if stack[-1] == "{" and now == "}":
                    stack.pop()
                elif stack[-1] == "[" and now == "]":
                    stack.pop()
                elif stack[-1] == "(" and now == ")":
                    stack.pop()
                else:
                    return False
        return not stack
        
    length : int = len(s)
    count : int = 0
    for shift in range(length):
        if isProper(s, shift):
            count += 1

    return count