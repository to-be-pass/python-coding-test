def solution(s):

    print(s)
    
    check = 0
    for i in s:
        if i == ')': 
            check += 1
        else:
            check -= 1
        
    if check == 0:
        return True
    else:
        return False
