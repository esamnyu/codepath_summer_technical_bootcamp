class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num_of_even = []
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                num_of_even.append(nums[i])
            else:
                continue
        return len(num_of_even)
        