def solution(s):
    # 97 == 1

    gyesoo = [0] * 26

    for i in s:
        gyesoo[ord(i) - 97] += 1


    result = ''


    for i in range(26):
        while int(gyesoo[i])>0:
            result+=chr(i+97)
            gyesoo[i]-=1

    return result
