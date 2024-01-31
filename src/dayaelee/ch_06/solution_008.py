def solution(s):
    # 소괄호가 정상으로 열고 닫혔는지 판별 
    # 정상 True, 비정상 False
    my_list = list(s)
    print(my_list)

    check = 0
    while(1):
        if len(my_list)==0:
             break
        
        if my_list.pop() == ")":
            check+=1
            
        else:
            check-=1

    if check == 0:
        return True
    else:
        return False