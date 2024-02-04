def solution(id_list, report, k):
    reporting_user = {}

    for line in report:
        uid, reported_id = line.split()
        if uid not in reporting_user:
            reporting_user[uid] = set([reported_id])
        else:
            reporting_user[uid].add(reported_id)
    
    reported_count = {}
    for _, reported_users in reporting_user.items():
        for reported_id in reported_users:
            if reported_id not in reported_count:
                reported_count[reported_id] = 1
            else:
                reported_count[reported_id] += 1

    answer = [0] * len(id_list)
    for i in range(len(id_list)):
        uid = id_list[i]
        if uid not in reporting_user:
            continue
        for reported_id in reporting_user[uid]:
            if reported_id in reported_count and reported_count[reported_id] >= k:
                answer[i] += 1
    return answer
