def solution(decimal):
    result = []
    while(1):
        
        if decimal//2 == 1:
            result.append(decimal % 2)
            result.append(1)
            break

        result.append(decimal % 2)
        decimal = decimal//2

    strr =''
    while(1):
        if len(result)==0:
            break
        else:
            strr+=str(result.pop())

    return strr