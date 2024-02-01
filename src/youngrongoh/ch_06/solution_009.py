def solution(decimal):
  stack = []
  value = decimal
  while value > 0:
    rest = value % 2
    stack.append(str(rest))
    value //= 2
  
  stack.reverse()
  return ''.join(stack)

