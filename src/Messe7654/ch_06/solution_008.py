def solution(s : str) -> bool:
    """올바른 괄호 문자열인지 판별하는 함수
    
    Args:
      s(str) : 괄호 문자열

    Returns:
      괄호가 올바르게 열리고 닫혔는지 여부

    """
    stack = []
    for c in s:
        if c == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False

    return not stack