def solution(s):
  stack = []
  for paren in s:
    if paren == ')':
      if len(stack) == 0: # 닫힌 괄호가 나왔을 때 스택이 비어있으면 무조건 False
        return False
      if stack.pop() == '(':
        continue
      else: # 닫힌 괄호가 나왔을 때 스택 top 값이 열린 괄호가 아니면 무조건 False
        return False

    stack.append(paren)
  return len(stack) == 0

"""
# 추가 테스트 케이스 1
- 입력: ')()'
- 이유: 열린 괄호가 스택에 하나도 없을 때 닫힌 괄호가 나온 경우 pop을 호출하거나 stack[-1]로 top을 조회하면 IndexError 발생
"""