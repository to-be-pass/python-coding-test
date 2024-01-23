def solution(prices):
  stack = list(reversed(prices))
  answer = []
  
  while stack:
    price = stack.pop()
    sec = 0
    for i in range(len(stack), 0, -1):
      sec += 1
      if price > stack[i-1]:
        break 
    answer.append(sec)
  return answer