def solution(n, k, cmd):
    table = [0] * n
    pointer = k
    delete_stack = []
    for c in cmd:
        if c[0] == 'U':
            pointer -= int(c[2:])
        elif c[0] == 'D':
            pointer += int(c[2:])
        elif c[0] == 'C':
            table.pop()
            delete_stack.append(pointer)
            if len(table) == pointer:
                pointer -= 1
        else:
            top = delete_stack.pop()
            table.append(0)
            if top <= pointer:
                pointer += 1
    while delete_stack:
        top = delete_stack.pop()
        table.insert(top, 1)

    return ''.join(['O' if x == 0 else 'X' for x in table])