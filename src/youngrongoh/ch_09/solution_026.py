def solution(nodes):
    return [preorder_traverse(nodes), inorder_traverse(nodes), postorder_traverse(nodes)]

def preorder_traverse(nodes):
    length = len(nodes)
    ptr = 0
    visited = [False] * length
    result = []
    while len(result) < length:
        parent = round((ptr - 1.5) / 2)
        left_idx = ptr * 2 + 1
        right_idx = ptr * 2 + 2

        if not visited[ptr]:
            visited[ptr] = True
            result.append(nodes[ptr])

        if left_idx < length and not visited[left_idx]:
            ptr = left_idx
            continue
        elif right_idx < length and not visited[right_idx]:
            ptr = right_idx
            continue
        elif parent >= 0:
            ptr = parent
        else:
            break;
    return ' '.join(map(str, result))

def inorder_traverse(nodes):
    length = len(nodes)
    ptr = 0
    visited = [False] * length
    result = []
    while len(result) < length:
        parent = round((ptr - 1.5) / 2)
        left_idx = ptr * 2 + 1
        right_idx = ptr * 2 + 2

        if left_idx < length and not visited[left_idx]:
            ptr = left_idx
            continue

        if not visited[ptr]:
            visited[ptr] = True
            result.append(nodes[ptr])

        if right_idx < length and not visited[right_idx]:
            ptr = right_idx
            continue

        if parent >= 0:
            ptr = parent
            continue
    return ' '.join(map(str, result))

def postorder_traverse(nodes):
    length = len(nodes)
    ptr = 0
    visited = [False] * length
    result = []
    while len(result) < length:
        parent = round((ptr - 1.5) / 2)
        left_idx = ptr * 2 + 1
        right_idx = ptr * 2 + 2

        if left_idx < length and not visited[left_idx]:
            ptr = left_idx
            continue
        elif right_idx < length and not visited[right_idx]:
            ptr = right_idx
            continue

        if not visited[ptr]:
            visited[ptr] = True
            result.append(nodes[ptr])

        right_of_parent = parent * 2 + 2
        if right_of_parent < length and not visited[right_of_parent]:
            ptr = right_of_parent
            continue

        if parent >= 0:
            ptr = parent
        else:
            break;
    return ' '.join(map(str, result))

