class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
    # sort the array of costs in non-decreasing order
        costs.sort()

        # initialize a counter for the number of ice cream bars
        count = 0

        # iterate through the array of costs
        for cost in costs:
            # if we have enough coins to buy the ice cream bar,
            # increment the counter and subtract the cost from our coins
            if coins >= cost:
                count += 1
                coins -= cost
            # if we don't have enough coins, return the counter
            else:
                return count

        # if we finish iterating through the array and have enough coins
        # left over, return the counter
        return count