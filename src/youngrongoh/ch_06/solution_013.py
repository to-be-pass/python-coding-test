def solution(board, moves):
  n = len(board)
  answer = 0
  stacks = [[] for _ in [0] * n]
  for i in range(n):
    for j in range(n):
      pos = board[n-1-j][i]
      if pos == 0:
        break
      stacks[i].append(pos)

  dolls = []
  for m in moves:
    stack = stacks[m - 1]
    if not stack:
      continue
    doll = stack.pop()
    if dolls and doll == dolls[-1]:
      dolls.pop()
      answer += 1
    else:
      dolls.append(doll)
  return answer * 2