def solution(board, moves):
  answer = 0
  stack = []
  for m in moves:
    j = m - 1
    doll = 0
    for i in range(len(board)):
      pos = board[i][j]
      if pos == 0:
        continue
      else:
        doll = pos
        board[i][j] = 0
        break
    if stack and doll == stack[-1]:
      stack.pop()
      answer += 2
      continue
    elif doll != 0:
      stack.append(doll)
  return answer