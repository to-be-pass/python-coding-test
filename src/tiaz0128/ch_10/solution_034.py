from collections import Counter


def solution(nums):
    counter = Counter(nums)

    return len(counter.most_common(len(nums) // 2))
