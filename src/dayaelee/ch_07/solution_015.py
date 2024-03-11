def solution(N, K):
    # 크기 N인 배열 만들기 
    tmpList = []

    for i in range(1, N+1):
        tmpList.append(i)

    print(tmpList)
    
    index = 1
    cnt = 1
    while(1):
        if len(tmpList) == 1:
            break

        if cnt == K:
            tmpList.pop(index-1)
            cnt = 1
            
        else :
            index += 1
            cnt+=1
            if index > len(tmpList):
                index = 1

    #print(tmpList)

    result = tmpList[0]

    # N이 마지막이 될 때까지 

    return result
