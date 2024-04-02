def pre(nodes, idx):
    if idx < len(nodes):
        ret = str(nodes[idx]) + " "
        ret += pre(nodes, idx * 2 + 1)
        ret += pre(nodes, idx * 2 + 2)
        return ret
    else:
        return ""

def inorder(nodes, idx):
    if idx < len(nodes):
        ret = inorder(nodes, idx * 2 + 1)
        ret += str(nodes[idx]) + " "
        ret += inorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""

def postorder(nodes, idx):
    if idx < len(nodes):
        ret = postorder(nodes, idx * 2 + 1)
        ret += postorder(nodes, idx * 2 + 2)
        ret += str(nodes[idx]) + " "
        return ret
    else:
        return ""

def solution(nodes):
    print('hi')
    return [
        pre(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1],
    ]
