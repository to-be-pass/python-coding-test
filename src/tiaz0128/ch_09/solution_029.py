from collections import defaultdict


def solution(enroll, referral, seller, amount):
    parent = dict(list(zip(enroll, referral)))
    total = defaultdict(int)

    for name, cnt in zip(seller, amount):
        money = 100 * cnt

        while money > 0 and name != "-":
            total[name] += money - money // 10
            name = parent[name]
            money //= 10

    return [total[name] for name in enroll]
