from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set: Sets contain unique values (no repetitions)
        # Sets in Python are unordered collections of unique elements
        tracker = set()
        for item in nums:
            if item in tracker:
                # The item exists in the tracker 
                return True
            else:
                # If we haven't seen this item in the tracker before, then add it, since there can only be unique (1 of each value) then we can use the set as a reference
                tracker.add(item)
        return False