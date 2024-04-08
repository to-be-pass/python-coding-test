from collections import defaultdict


def solution(graph, start):

    node_tree = defaultdict(list)
    for i, v in graph:
        node_tree[i].append(v)

    
    def dfs(node, visited, result):  
        visited.add(node)
        result.append(node)
        for injeop in node_tree.get(node, []):
            if injeop not in visited:
                dfs(injeop, visited, result)   
    # 결과 
    visited = set()
    result = []
    dfs(start, visited, result)

    return result