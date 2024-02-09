import math
from collections import defaultdict


def solution(enroll, referral, seller, amount):

    inheritance = list(zip(enroll[::-1], referral[::-1]))

    amount_by_seller = defaultdict(int)
    for name, cnt in zip(seller, amount):
        amount_by_seller[name] += 100 * cnt

    for enr, ref in inheritance:
        income = math.floor(amount_by_seller[enr] * 0.1)

        amount_by_seller[enr] -= income
        amount_by_seller[ref] += income

    return [amount_by_seller.get(name, 0) for name in enroll]
