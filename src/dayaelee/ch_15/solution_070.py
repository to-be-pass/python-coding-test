from collections import deque
def solution(str1, str2):

    # 최장 공통 부분 수열의 길이를 계산

      # str1먼저, str2

    i, j = 0, 0

    s1 = len(str1)
    s2 = len(str2)

    cnt = 0
    check = 0
    while 1:
        if i == s1:
            if j < s2:
                if check ==1:
                    i = originI 
                    j = originJ+1 
                    check = 0
                else:
                    j+=1
                    i = originI
            else:
                break

        if str1[i] == str2[j]:
            cnt+=1
            i +=1
            j +=1
            check = 1
            originI = i
            originJ = j
        else:
            i+=1

    cnt2 = 0
    i, j = 0, 0

    check = 0
    cnt2 = 0
    while 1:
        if j == s2:
            if i < s1:
                if check == 1:
                    i = originI +1
                    j = originJ
                    check = 0
                else:
                    i+=1
                    j = originJ

            else:
                break

        if str1[i] == str2[j]:
            cnt2 += 1
            i +=1
            j +=1
            originI = i
            originJ = j
            check = 1
            if originJ == s2:
                break
        else:
            j+=1
    return  max(cnt, cnt2)
