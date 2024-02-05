def is_valid_matrix(n):
    if n < 5 or n > 30:
        raise Exception('보드의 범위가 올바르지 않습니다.')

def rotate_matrix(arr):
    return [list(col) for col in zip(*arr)]
    
# moves 배열의 크기는 1 이상 1,000 이하입니다.
def solution(board, moves):
    # 보드 범위 확인
    is_valid_matrix(len(board))

    state = rotate_matrix(board)
    stack = []
    result = 0 
    select = 0
    for m in moves:
        index = m - 1
        while len(state[index]) > 0:
            select = state[index].pop(0)
            if select != 0:               
                break
        if stack and stack[-1] == select :
            stack.pop()
            result += 1
        else:
            stack.append(select)
        

    return result



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	
print(solution(board, moves))