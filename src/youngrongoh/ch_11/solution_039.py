from collections import defaultdict, deque

def solution(graph, start):
    adj_list = defaultdict(list)
    for a, b in graph:
        adj_list[a].append(b)
    
    answer = []
    visited = set()
    queue = deque([start])

    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        answer.append(curr)
        for adj in adj_list[curr]:
            queue.append(adj)
    return answer
