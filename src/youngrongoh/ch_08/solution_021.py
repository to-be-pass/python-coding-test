def solution(want, number, discount):
    # 상품에 대한 수량 매핑
    shopping_list = {}
    for i in range(len(want)):
        shopping_list[want[i]] = number[i]

    answer = 0
    for i in range(len(discount) - 9):
        # 10개 씩 할인 상품 개수 테이블 만들어서 원하는 상품 모두 살 수 있는지 비교
        discount_list = {}
        for j in range(i, i + 10):
            p = discount[j]
            if p in discount_list:
                discount_list[p] += 1
            else:
                discount_list[p] = 1
        if discount_list == shopping_list:
            answer += 1

    return answer

