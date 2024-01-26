# 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다.
#
# [1,5,3,5,1,2,1,4]
#
# [[0,0,0,0,0],
#  [0,0,1,0,3],
#  [0,2,5,0,1],
#  [4,2,4,4,2],
#  [3,5,1,3,1]]


def solution(board, moves):
    # 1. 주어진 형태를 좀더 쉽게 풀기 위해 zip 을 쓰자
    game = list(map(list, zip(*board)))
    stack = []
    cnt = 0

    # 2. zip으로 만든 배열에서 0이 아닌값을 꺼내서 0으로 바꾼다
    for move in moves:
        column = game[move - 1]

        for i in range(len(column)):
            # 0이 아닌 = 인형이 있으면
            if doll := column[i]:
                column[i] = 0
                # stack에 최상단과 현재 인형이 같은 경우
                if stack and stack[-1] == doll:
                    stack.pop()
                    # 인형 한번에 두개 없어지니까 +2
                    cnt += 2
                else:
                    stack.append(doll)
                break

    return cnt
