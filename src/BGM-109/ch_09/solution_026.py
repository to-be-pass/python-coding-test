def pre_order(nodes, i):
    result = ""
    left = 2 * i + 1
    right = 2 * i + 2
    if i < len(nodes):
        result = f"{nodes[i]} "
        result += pre_order(nodes, left)
        result += pre_order(nodes, right)
        return result

    return ""

def in_order(nodes, i):
    result = ""
    left = 2 * i + 1
    right = 2 * i + 2
    if i < len(nodes):
        result = in_order(nodes, left)
        result += f"{nodes[i]} "
        result += in_order(nodes, right)
        return result

    return ""


def post_order(nodes, i):
    result = ""
    left = 2 * i + 1
    right = 2 * i + 2
    if i < len(nodes):
        result = post_order(nodes, left)
        result += post_order(nodes, right)
        result += f"{nodes[i]} "
        return result

    return ""




def solution(nodes):
    return [
        pre_order(nodes, 0)[:-1],
        in_order(nodes, 0)[:-1],
        post_order(nodes, 0)[:-1]
    ]



nodes = [1, 2, 3, 4, 5, 6, 7]
result = solution(nodes)
print(result)