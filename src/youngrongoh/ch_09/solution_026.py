def solution(nodes):
    return [' '.join(preorder_traverse(nodes, 0)), ' '.join(inorder_traverse(nodes, 0)), ' '.join(postorder_traverse(nodes, 0))]

def preorder_traverse(nodes, idx):
    result = []
    if idx < len(nodes):
        result.append(str(nodes[idx]))
        result.extend(preorder_traverse(nodes, idx * 2 + 1))
        result.extend(preorder_traverse(nodes, idx * 2 + 2))
    return result

def inorder_traverse(nodes, idx):
    result = []
    if idx < len(nodes):
        result.extend(inorder_traverse(nodes, idx * 2 + 1))
        result.append(str(nodes[idx]))
        result.extend(inorder_traverse(nodes, idx * 2 + 2))
    return result

def postorder_traverse(nodes, idx):
    result = []
    if idx < len(nodes):
        result.extend(postorder_traverse(nodes, idx * 2 + 1))
        result.extend(postorder_traverse(nodes, idx * 2 + 2))
        result.append(str(nodes[idx]))
    return result
