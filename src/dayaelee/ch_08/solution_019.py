def solution(string_list, query_list):
    # 각 쿼리 리스트에 있는 문자열이 stringList의 문자열 리스트에 있는지 여부를 확인해야함 

    hashtable = [0] * (len(string_list))

    # 해시 테이블 생성, string_list가 들어있음 
    for i in range(len(string_list)):
        hashtable[i] = hashing(string_list[i])

    result = []

    for i in range(len(query_list)):
        if hashing(query_list[i]) in hashtable:
            result.append(True)
        else:
            result.append(False)
    return result

def hashing(string):

    m = 1_000_000_007
    sum = 0
    for i in range(len(string)):
        if i == 0:
            sum += ord(string[i])
        else: 
            sum += ord(string[i]) * (31**i) 

    sum = sum % m
    return sum