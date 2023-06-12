from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge Case: Empty array: Output 0
        if len(nums) == 0:
            return 0

        # 1. Remove duplicates by converting nums to a set and sort it
        sorted_array = sorted(set(nums))

        # 2. Initialize counters
        longest_sequence = 1  # The longest sequence found so far, set to 1 because a single number is also a sequence
        current_sequence = 1  # The current sequence being counted

        # 3. Iterate over sorted_array starting from the second element
        for i in range(1, len(sorted_array)):
            # 4. If the current number is consecutive to the previous one, increment the current sequence counter
            if sorted_array[i] == sorted_array[i-1] + 1:
                current_sequence += 1
            else:
                # 5. If the numbers are not consecutive, then the current sequence has ended
                # Check if the current sequence is longer than the longest sequence found so far
                if current_sequence > longest_sequence:
                    # If so, update longest_sequence
                    longest_sequence = current_sequence

                # 6. Reset current_sequence to 1 for the next sequence
                # Important for cases like [1, 2, 3, 5, 6, 7]
                # We are comparing pairs of consecutive numbers and the last pair is (3, 5), this evaluates to 5 > 3 + 1
                current_sequence = 1

        # 7. After the loop, do one final check to see if the last sequence is the longest
        if current_sequence > longest_sequence:
            longest_sequence = current_sequence

        # 8. Return the length of the longest consecutive sequence
        return longest_sequence

# Test the function with some input
if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Should print 4
    print(s.longestConsecutive([1, 2, 3, 5, 6, 7])) # Should print 3, not 5
