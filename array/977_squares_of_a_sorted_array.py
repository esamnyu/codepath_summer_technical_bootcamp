class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_squares = []
        for i in range(len(nums)):
            sorted_squares.append(int(nums[i]**2))
        return sorted(sorted_squares)
        