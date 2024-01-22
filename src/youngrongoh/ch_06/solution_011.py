def solution(s):
  stack = []
  for char in s:
    if stack:
      top = stack[-1]
      if char == top:
        stack.pop()
        continue
    stack.append(char)

  if stack:
    return 0
  else:
    return 1