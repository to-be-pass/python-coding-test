from collections import deque


def solution(card1, card2, goal):
    goal_q = deque(goal)
    card1_q = deque(card1)
    card2_q = deque(card2)
    n = len(goal)
    while n > 0:
        word = goal_q.popleft()
        
        if len(card1_q) > 0 and word == card1_q[0]:
            card1_q.popleft()
        elif len(card2_q) > 0 and word == card2_q[0]:
            card2_q.popleft()
        else:
            goal_q.append(word)
            
        n -= 1
    
    return "Yes" if len(goal_q) == 0 else "No"



cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1,cards2,goal))
