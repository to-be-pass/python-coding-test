import math
def solution(string_list, query_list):
    answer = []
    hash_table = {}
    for string in string_list:
        hash_table[hash(string)] = 1

    for q in query_list:
        answer.append(True if hash(q) in hash_table else False)
    return answer

def hash(string):
    hash_key = 0
    for i in range(len(string)):
        char = string[i]
        hash_key += ord(char) * math.pow(31, i)
    return hash_key % 1000000007
