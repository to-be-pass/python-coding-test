from collections import deque
def solution(card1, card2, goal):
    queue1 = deque(card1)
    queue2 = deque(card2)

    answer = True
    for word in goal:
        if queue1 and word == queue1[0]:
            queue1.popleft()
        elif queue2 and word == queue2[0]:
            queue2.popleft()
        else:
            answer = False
            break
        
    return 'Yes' if answer else 'No'
