def solution(s):
  stack = []
  for paren in s:
    if paren == ')' and stack[-1] == '(':
      stack.pop()
      continue
    stack.append(paren)
  return len(stack) == 0
