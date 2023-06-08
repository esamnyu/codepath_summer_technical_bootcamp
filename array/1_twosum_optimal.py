from typing import List 
def twoSum(nums, target):
    tracker = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in tracker:
            return [tracker[complement], i]
        tracker[num] = i
    return []

# Test the function with a list of numbers and a target
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target)) # This should print [0, 1]
