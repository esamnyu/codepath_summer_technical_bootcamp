class Solution:
    def isHappy(self, n: int) -> bool:
        # Keep track of previously seen numbers to detect a loop
        seen_numbers = set()

        # Repeatedly compute the sum of the squares of the digits
        # until we reach 1 or enter a loop
        while n != 1:
            # If we've seen this number before, it means we're in a loop
            # and n is not a happy number
            if n in seen_numbers:
                return False
            seen_numbers.add(n)

            # Compute the sum of the squares of the digits
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            n = total

        # If we've reached this point, it means n is a happy number
        return True
