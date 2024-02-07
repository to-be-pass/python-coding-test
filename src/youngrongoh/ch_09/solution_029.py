def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    salary = { name: 0 for name in enroll }
    for i in range(len(seller)):
        curr = seller[i]
        money = amount[i] * 100
        while money > 0 and curr != '-':
            salary[curr] += money - money // 10
            money //= 10
            curr = parent[curr]

    return [salary[name] for name in enroll]