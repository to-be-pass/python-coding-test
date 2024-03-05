def solution(graph, start):
    nodes = {}
    for [a, b] in graph:
        if a not in nodes:
            nodes[a] = { 'key': a, 'adj': [], 'visited': False }
        if b not in nodes:
            nodes[b] = { 'key': b, 'adj': [], 'visited': False }
        nodes[a]['adj'].append(b)
    
    stack = [start]
    visit_order = []
    while stack:
        node = nodes[stack.pop()]
        if node['visited']:
            continue
        node['visited'] = True
        stack.extend(sorted(node['adj'], reverse=True))
        visit_order.append(node['key'])
    return visit_order
