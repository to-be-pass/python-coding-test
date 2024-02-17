from typing import List


def find(parents: List[int], target: int):
    # 2. 부모 노드가 루트 노드인지 확인 (index == value)
    if parents[target] == target:
        return target

    # 3. 아닌 경우 계속해서 부모 노드를 타고 올라간다.
    parents[target] = find(parents, parents[target])
    return parents[target]


def union(parents: List[int], x, y):
    # 1. 각각 루트 노드를 찾는다.
    root_x = find(parents, x)
    root_y = find(parents, y)

    # 2. 찾은 루트 노드의 크기를 비교
    parents[root_y] = root_x


def solution(k, operations):
    parents = list(range(k))

    for operator, *nodes in operations:
        if operator == "u":
            union(parents, *nodes)
        elif operator == "f":
            find(parents, *nodes)

    return len(set(find(parents, i) for i in range(k)))
