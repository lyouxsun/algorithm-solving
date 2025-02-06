def solution(nums):
    n = len(nums) // 2
    nums_set = set(nums)
    print(nums_set)
    if len(nums_set) < n:
        return len(nums_set)
    return n