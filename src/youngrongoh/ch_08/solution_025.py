def solution(orders, course):
    combs_by_size = { size: {} for size in course }

    for order in orders:
        sorted_order = ''.join(sorted(order))
        length = len(sorted_order)
        prev_combs = list(sorted_order)
        for size in range(2, length + 1):
            if size not in combs_by_size:
                combs_by_size[size] = {}

            curr_combs = []
            for prev_comb in prev_combs:
                i = sorted_order.index(prev_comb[-1]) + 1
                for j in range(i, length):
                    comb = prev_comb + sorted_order[j]
                    if comb not in combs_by_size[size]:
                        combs_by_size[size][comb] = 0
                    combs_by_size[size][comb] += 1
                    curr_combs.append(comb)
            prev_combs = curr_combs
    answer = []
    for size in course:
        max_count = 0
        selected_combs = []
        for comb, count in combs_by_size[size].items():
            if count < 2:
                continue
            if count > max_count:
                selected_combs = [comb]
                max_count = count
            elif max_count == count:
                selected_combs.append(comb)
        answer.extend(selected_combs)
    return sorted(answer)
