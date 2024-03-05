def solution(graph, start):
    nodes = {}
    for [a, b] in graph:
        if a not in nodes:
            nodes[a] = { 'adj': [], 'visited': False }
        if b not in nodes:
            nodes[b] = { 'adj': [], 'visited': False }
        nodes[a]['adj'].append(b)
    
    answer = []
    dfs(nodes, start, answer)
    return answer

def dfs(nodes, curr, result):
    if nodes[curr]['visited']:
        return
    else:
        nodes[curr]['visited'] = True
        result.append(curr)
        for key in nodes[curr]['adj']:
            dfs(nodes, key, result)
        return