def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        row = [0] * (len(arr2[0]))
        for j in range(len(arr2)):
            for k in range(len(arr2[0])):
                row[k] += arr1[i][j] * arr2[j][k]
        result.append(row)
    return result