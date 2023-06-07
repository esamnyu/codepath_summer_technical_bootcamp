class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # nums: List[int] is a type hint- the expected value of the type as interpreted by python
    # Steps to solve: Sort the array first so that the max values and the min values are seen 
    # filtered array contains values 
        filtered_nums = []
        for item in nums:
            if item <= target:
                filtered_nums.append(item)
        # This is a n^2 time complexity operation 
        for i, item in enumerate(nums):
            # Take into account the current index + the following index 
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j] 

    


