def solution(k, operations):
    def find(nodeList, target):
        if nodeList[target] and target != nodeList[target]:
            result = nodeList[target]
            find(nodeList, result)
        return target

    nodeList = []

    for i in range(0, k):
        nodeList.append(i)


    for i in operations:

        if i[0] == 'u':
            if i[1] < i[2]:
                idx = i[1]
                toIdx = i[2]
                nodeList[idx] = nodeList[toIdx]
            else:
                idx = i[2]
                toIdx = i[1]
                nodeList[idx] = nodeList[toIdx]

        elif i[0] == 'f':
            rootNode = find(nodeList, i[1])
            

    cnt = 0
    for i in range(0, len(nodeList)):
        if nodeList[i] == i:
            cnt+=1
    

    return cnt
