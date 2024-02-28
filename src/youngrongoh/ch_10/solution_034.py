def solution(nums):
    pick_count = len(nums) / 2
    kinds = set(nums)
    kinds_count = len(kinds)
    return min(kinds_count, pick_count)
