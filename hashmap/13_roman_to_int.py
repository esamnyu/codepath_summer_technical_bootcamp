class Solution:
    def romanToInt(self, s: str) -> int:
        # Use a dictionary to perform mappings 
        numerals = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L': 50, 
            'C':100, 
            'D':500, 
            'M':1000
            }
        # Understand the Subtraction rule in Roman Numerals 
        # If a smaller number appears in front of a larger number, subtract the smaller number 
        total = 0
        previous = 0

        for char in s:
            current = numerals[char]
        
        # If the current numeral is greater than the previous we've encountered a situation where subtraction is needed (Like) IV or IX
        # We have previously added the value of the smaller numeral to the total, so we needto subtract it twice before adding the value of 
        # The larger numeral  
        # Our program evaluates IV as 6 because we keep expecting candies, so we subtract 2, to get it back down to 4 
            if current > previous:
                total = total - 2 * previous 
            # Add the value of the current numeral to the total
            total = total + current 
            # Update the previous numeral for the next iteraiton 
            previous =  current
        # After the loop, the total will hold the integer equivalent if the input Roman numeral string 
        return total