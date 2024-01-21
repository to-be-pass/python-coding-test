def solution(decimal):
  stack = []
  value = decimal
  while value > 1:
    rest = value % 2
    stack.append(rest)
    value = value // 2
  stack.append(value)

  result = ''
  while stack:
    result += str(stack.pop())
  return result
