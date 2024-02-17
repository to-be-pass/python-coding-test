def solution(nums):
    num_set = set(nums)
    k = len(nums) // 2

    return min(len(num_set), k)
