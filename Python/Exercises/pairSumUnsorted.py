## Given an array of integers, return the indexes of any two numbers that add up to a target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array
nums = [-1, 3, 4, 2]
def pair_unsorted(arr: list) -> list:
    target = 3
    nums_map = {}
    for index,num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], index]
        nums_map[num] = index
    return []

print(pair_unsorted(nums))