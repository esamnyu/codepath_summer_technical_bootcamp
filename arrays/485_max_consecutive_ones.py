class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        result = []
#         We need to append to the end of the List a 0 so that we know where to demarcate the last instance of multiples of 1 
        nums.append(0)
        # for i in range(0, len(nums)): -> start and stop 
        for i in range(len(nums)):
            # Previously used for i in nums -? i is equal to the value at that index, so we're referencing index the value at index 0 or 1 which would always be 1
            # print(nums[i])
            if nums[i]==1:
                count+=1
            else:
#               Append all multiple instances of 1 into in the result array 
                result.append(count)
                count = 0
        return max(result)
