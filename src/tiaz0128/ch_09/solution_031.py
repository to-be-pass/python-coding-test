from collections import deque


def build_tree(info, edges):

    tree = [[] for _ in info]

    for parent, child in edges:
        tree[parent].append(child)

    return tree


def bfs(info, tree):
    max_sheep = 0
    # 현재 위치, 양의 수, 늑대 수, 방문한 노드?
    queue = deque([(0, 1, 0, set())])

    while queue:
        current, sheep_count, wolf_count, visited = queue.popleft()
        max_sheep = max(max_sheep, sheep_count)
        visited.update(tree[current])

        for next_node in visited:
            if info[next_node] == 1:
                if sheep_count > wolf_count + 1:
                    queue.append(
                        (next_node, sheep_count, wolf_count + 1, visited - {next_node})
                    )
            else:
                queue.append(
                    (next_node, sheep_count + 1, wolf_count, visited - {next_node})
                )
    return max_sheep


def solution(info, edges):
    tree = build_tree(info, edges)
    # for idx, row in enumerate(tree):
    #     print(idx, row)

    return bfs(info, tree)
