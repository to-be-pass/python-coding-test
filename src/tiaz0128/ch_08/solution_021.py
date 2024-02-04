from collections import Counter


def solution(want, number, discount):
    answer = 0

    wanted_items = {want[idx]: cnt for idx, cnt in enumerate(number)}

    for idx, item in enumerate(discount):
        items = discount[idx : idx + 10]
        counter = Counter(items)

        if all(
            [
                cnt <= counter.get(category, False)
                for category, cnt in wanted_items.items()
            ]
        ):
            answer += 1

    return answer
