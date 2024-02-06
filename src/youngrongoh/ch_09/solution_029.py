def solution(enroll, referral, seller, amount):
    seller_amount = dict(zip(seller, amount))
    parent_rel = dict(zip(enroll, referral))
    totals = { name: 0 for name in enroll }
    for name in enroll:
        sale = 0
        if name in seller_amount:
            sale = seller_amount[name] * 100
        curr = name
        while sale > 0 and curr != '-':
            totals[curr] += sale - sale // 10
            sale = sale // 10
            curr = parent_rel[curr]
    return list(totals.values())
