from collections import deque


def solution(card1, card2, goal):
    d_c1 = deque(card1)
    d_c2 = deque(card2)

    for word in goal:
        if d_c1 and word == d_c1[0]:
            d_c1.popleft()
        elif d_c2 and word == d_c2[0]:
            d_c2.popleft()
        else:
            return "No"

    return "Yes"
