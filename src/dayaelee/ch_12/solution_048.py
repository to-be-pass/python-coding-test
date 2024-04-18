def solution(board):
    def areYouInBoX(check1, value, idx, idxx, board):
        row = (idx // 3) * 3
        col = (idxx // 3) * 3
        for t in range(row, row+3): # 행
            for tt in range(col, col+3): # 열
                if board[t][tt] == value:
                    check1 = 1
                    return check1 # 3 * 3안에 존재한다. 
                else:
                    continue
        return check1

    def inRow(check2, value, idxx, board):
        for t in range(0, 9): #행
            if board[t][idxx] == value:
                check2 = 1
                return check2
            else:
                continue
        return check2

    def inCol(check3, value, idx, board):
        for tt in range(0, 9): # 열
            if board[idx][tt] == value:
                check3 = 1
                return check3
            else:
                continue
        return check3

    def find_empty_position():
        for idx in range(0, 9): # 행
            for idxx in range(0, 9): #열
                if board[idx][idxx] != 0: 
                    # 이미 값이 있는가? 
                    continue
                else: 
                    # 해당 자리에 값이 없는 경우 == 0
                    return idx, idxx
        return None
                


    def find_solution():
        empty_pos = find_empty_position() 
        if not empty_pos:
            return True
        idx, idxx = empty_pos
        for value in range(1, 10):
            # if value not in nList:
            check1 = 0 
            check2 = 0
            check3 = 0
            check1 = areYouInBoX(check1, value, idx, idxx, board)
            check2 = inRow(check2, value, idxx, board)
            check3 = inCol(check3, value, idx, board)
            if check1 == 0 and check2 ==0 and check3==0:
                board[idx][idxx] = value
                if find_solution():
                    return True
                board[idx][idxx] = 0
        return False



    find_solution()           

    # print('')
    # for ii in board:
    #     print(ii)

    return board
    
