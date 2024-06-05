import copy
def solution(arr, n):

    maxN = len(arr)

    tmp = [ ([0]*maxN) for i in range(maxN)]

    while n> 0:
        for i in range(maxN):
            for j in range(maxN):
                tmp[i][j] = arr[(maxN-1)-j][i]

        arr = copy.deepcopy(tmp)
        n-=1
    
    # hi 


    return tmp


