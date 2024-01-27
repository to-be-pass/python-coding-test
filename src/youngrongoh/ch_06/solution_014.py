def solution(n, k, cmd):
    up = [i - 1 for i in range(n + 2)]  
    down = [i + 1 for i in range(n + 2)]
    pointer = k + 1

    deleted = []
    for c in cmd:
        if c == 'C':
            down[up[pointer]] = down[pointer]
            up[down[pointer]] = up[pointer]
            deleted.append(pointer)
            pointer = down[pointer] if down[pointer] <= n else up[pointer]
        elif c == 'Z':
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        else:
            [dir, amount] = c.split()
            for _ in range(int(amount)):
                if dir == 'U':
                  pointer = up[pointer]
                else:
                  pointer = down[pointer]
    print(deleted)
    result = ['O'] * n
    for i in deleted:
        result[i - 1] = 'X'
    return ''.join(result)