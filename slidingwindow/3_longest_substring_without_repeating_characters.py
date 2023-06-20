class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # The letters in the substring must all be unique 
        # # Constraints are 0 <= s.length <= 5 * 104
        
        # # Edge Case 1: [Constraints] Take into account empty strings
        # if len(s) == 0:
        #     return 0
        # storage = set() # "Storage is made into a set for O(1) lookups   
        # # Let's consider a two pointer approach, such as the one that was used in longest sequence
        # # Initialize the two pointers
        # # Sliding window approach 
        # max_length = 0
        # l, r = 0, 0 
        # while l < len(s) and r < len(s):
        #     if s[r] not in storage:
        #         # increment if character in string is seen in storage: means we've seen this char before 
        #         r +=1
        #         max_length = max(max_length, r-1)
        #     # Unique substring, so continue to look forward 
        #     else:
        #         # increment 'l' if character in string is seen in storage: means we've seen this char before
        #         storage.remove(s[l])
        # return max_length

        # Take care of the edge case 
        if len(s) == 0:
            return 0
        index_map = {} # Keep track of the indices and their associated values 
        max_len = 0 
        start = 0

        for i, char in enumerate(s):
            if char in index_map:
                # Move the start pointer to right after the previous occurence  
                start = max(index_map[char]+1, start)
            index_map[char] = i # Update the index of the current character (key/value pair)
            cur_len = i - start + 1 # Calculate the length of the current substring 
            max_len = max(max_len, cur_len) # Update max_len if necessary 
        return max_len 



