def solution(matrix1, matrix2):

    n = len(matrix1)
    m = len(matrix2[0])

    newMat = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(n):
        
        for q in range(n):
            sum = 0
            for j in range(m):
                sum += matrix1[i][j] * matrix2[j][q]
                if j == m-1:
                    newMat[i][q] = sum

    tmp = 0
    
    check = []

    for i in range(n):
        for j in range(m):
            if i == j:
                pass
            else:
                check2 = 1
                for kk in check:
                    if kk == [i, j]:
                        check2 = 0
                        break
                
                if check2 == 0:
                    continue
                    
                tmp = newMat[i][j]
                newMat[i][j] = newMat[j][i]
                newMat[j][i] = tmp

                check.append([j, i])

    return newMat
