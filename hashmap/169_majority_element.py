# Import the List class from the typing module, which allows you to use List[int] as a type hint for the nums parameter in your majorityElement method.
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    # Create a dict to keep track of the number of each item in nums {
        # Initialize an empty dictionary
        # Key -> Value
        count_of_num = {}
        # Your list of items
        items = nums

        # Loop through the list
        for item in items:
            if item in count_of_num:
                # If the item is already in the dictionary, increment its value
                count_of_num[item] += 1
            else:
                # If the item is not in the dictionary, add it with a value of 1
                count_of_num[item] = 1

        # Print the dictionary
        for item, count in count_of_num.items():
            if count_of_num[item] > len(nums)/2:
                return item
            
# Create an instance of the class
solution = Solution()

# Call the instance of the class 
print(solution.majorityElement([2,2,1,1,1,2,2]))

        


        
    
            