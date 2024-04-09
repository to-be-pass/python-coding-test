def solution(graph, source):

    vLen = len(graph)
    distances = [float("inf")] * vLen
    distances[source] = 0
    predecessor = [None] * vLen

    # 최단 경로 구하기 

    for tmp in range(0, vLen-1):
        for v, nodeSet in enumerate(graph):
            for injeopNodeSet in nodeSet:
                injeopNode, weight = injeopNodeSet
                distance = distances[v] + weight
                if distance < distances[injeopNode]:
                    distances[injeopNode] = distance
                    predecessor[injeopNode] = v
    
    # 음의 순환 구하기 
                    
    for v, nodeSet in enumerate(graph):
        for injeopNodeSet in nodeSet:
            injeopNode, weight = injeopNodeSet
            distance = distances[v] + weight
            if distance < distances[injeopNode]:
                return [-1]

    return [distances, predecessor]

