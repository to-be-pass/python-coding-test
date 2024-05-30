from collections import deque

def solution(arr1, arr2):

    arr1 = deque(arr1)
    arr2 = deque(arr2)

    sortedList = []

    while 1:
        if len(arr1) == 0 and len(arr2) == 0:
            break
        
        if len(arr1)>0 and len(arr2)>0:
            if arr1[0] < arr2[0]:
                value = arr1.popleft()
                sortedList.append(value)
            elif arr1[0] > arr2[0]:
                value = arr2.popleft()
                sortedList.append(value)
            else:
                value1 = arr1.popleft()
                value2 = arr2.popleft()
                sortedList.append(value1)
                sortedList.append(value2)
        else:
            while len(arr1)>0:
                value = arr1.popleft()
                sortedList.append(value)
            
            while len(arr2)>0:
                value = arr2.popleft()
                sortedList.append(value)
            

    return sortedList
