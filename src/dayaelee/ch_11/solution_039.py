from collections import defaultdict, deque

def solution(graph, start):
    # 트리 생성
    tmp_tree = defaultdict(list)
    for i, v in graph:
        tmp_tree[i].append(v)

    def BFS(start):
        visited.add(start)
        result.append(start)
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for injeop in tmp_tree.get(node, []):
                if injeop not in visited:
                    visited.add(injeop)
                    result.append(injeop)
                    queue.append(injeop)



    result=[]
    visited = set()
    BFS(start)

    return result
