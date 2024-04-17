def solution(N):

    results = []
    def backtrack(sum, selected_num, start):
        if sum == 10:
            
            results.append(selected_num)
            print(selected_num)
            return

        for i in range(start, N+1):
            if i + sum <=10:
                backtrack(i + sum, selected_num + [i], i + 1)

    backtrack(0, [], 1)
    print(results)
    return results
