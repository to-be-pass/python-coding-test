def solution(s):
  answer = 0
  
  for x in range(len(s)):
    # 문자열 회전
    turned = s[x:] + s[:x]
    if check_right(turned):
      answer += 1
  
  return answer

openings = ('(', '{', '[')
couples = {
    ')': '(',
    '}': '{',
    ']': '[',
}

def check_right(s):
  stack = []
  for paren in s:
    if paren in openings:
      stack.append(paren)
      continue

    # 닫는 괄호인 경우
    if stack: # 스택이 비어있는데 top 조회하면 IndexError 발생하므로 체크
      top = stack[-1]
      # 스택 top과 닫는 괄호가 짝이 맞으면 스택에서 상쇄
      if top == couples[paren]:
        stack.pop()
    # 닫는 괄호가 나왔는데 스택이 비어있으면 항상 False
    else:
      return False

  return len(stack) == 0
