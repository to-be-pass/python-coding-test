def solution(lst, search_lst):
    tree = []
    for value in lst:
        insert(tree, value, 0)
    answer = []
    for value in search_lst:
        answer.append(find(tree, value, 0))
    return answer


def find(tree, value, idx):
    if idx >= len(tree) or not tree[idx]:
        return False
    
    if tree[idx] > value:
        return find(tree, value, idx * 2 + 1)
    elif tree[idx] < value:
        return find(tree, value, idx * 2 + 2)
    else:
        return True

def insert(tree, value, idx):
    if idx >= len(tree) or not tree[idx]:
        blank = idx - (len(tree) - 1)
        if blank > 0:
            tree.extend([None] * blank)
        tree[idx] = value
        return

    if tree[idx] > value:
        insert(tree, value, idx * 2 + 1)
    else:
        insert(tree, value, idx * 2 + 2)
    return

