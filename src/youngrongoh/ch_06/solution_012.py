def solution(prices):
  answer = [0] * len(prices)
  
  stack = [0]
  for i in range(1, len(prices)):
    while stack and prices[stack[-1]] > prices[i]:
      top = stack.pop()
      answer[top] = i - top
    stack.append(i)

  while stack:
    top = stack.pop()
    answer[top] = len(prices) - 1 - top
  return answer