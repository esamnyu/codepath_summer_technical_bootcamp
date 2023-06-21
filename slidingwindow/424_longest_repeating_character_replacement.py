class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize count dictionary to keep track of character frequencies in the window
        count = {}

        # Initialize variables: 
        # res to store the maximum length of the substring 
        # l to indicate the left boundary of the window
        # maxf to store the max frequency of any character within the window
        res = 0
        l = 0
        maxf = 0 

        # Iterate over the string using r as the right boundary of the window
        for r in range(len(s)):
            # Update the count of the current character
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Update maxf to the maximum frequency so far
            maxf = max(maxf, count[s[r]])
            
            # Check if the number of replacements required (size of the window minus max frequency) 
            # is greater than k, if yes then we need to shrink the window
            while(r - l + 1) - maxf > k:
                # Decrease the count of the leftmost character of the window as we are moving it forward
                count[s[l]] -=1
                
                # Move the left boundary of the window
                l+=1
            
            # Update res to maximum length of the valid window so far
            res = max(res, r - l + 1)
        
        # Return the length of longest valid substring
        return res
