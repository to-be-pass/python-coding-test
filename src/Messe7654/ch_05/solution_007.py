def isIn(coord):
    x, y = coord
    return -5 <= x and x <= 5 and -5 <= y and y <= 5

def solution(dirs):
    history = set() # stores before <-> after
    xpos, ypos = 0, 0

    for movement in dirs:
        if movement == "U":
            after = (xpos, ypos - 1)
        elif movement == "L":
            after = (xpos - 1, ypos)
        elif movement == "D":
            after = (xpos, ypos + 1)
        else:
            after = (xpos + 1, ypos)
        if isIn(after):
            before = (xpos, ypos)
            xpos, ypos = after
            history.add((before, after))
            history.add((after, before))

    return len(history) // 2
