from collections import defaultdict

def solution(graph, start):

    adj_list = defaultdict(list)

    for u, v in graph:
        adj_list[u].append(v)


    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)
        for neighbor in adj_list.get(node, []):
            print('neighbor', neighbor)

            if neighbor not in visited:
                dfs(neighbor, visited, result)

    visited=set()
    result = []
    dfs(start, visited, result)

    return result 

