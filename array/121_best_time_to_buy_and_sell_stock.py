class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Save the differences in a dictionary or array? 
        # Make sure that the progression is from lesser to greater when traversing the array 
        # Can we use two pointers with both pointers starting from the beginning? 
        # Iterate the array  
        # Lets make money babyyyy
        # key- current index, value - all the possible profits from this point(list) 
        # Dont need i and j, just need a single pass 
        # min_value = min(prices)
        # location = 
        # current_price = 0
        # max_profit = 0 
        # for i in range(len(prices)-1):  
        #     current_price = prices[i]
        #     if current_price <  


        #     if current_profit > max_profit:
        #         max_profit = current_price 
        #     else:
        #         j+=1
        #         continue
        #     i+=1
        # return max_profit
        # j = 0
        # max_diff = 0
        # current_diff = 0
        # min_value = min(prices)
        # for i in range(len(prices)-1):
        #     if prices[i] == min_value:
        #         j = i  
        #         current_diff = prices[j+1] - prices[i]  
        #         if current_diff > max_diff:
        #             max_diff = current_diff
        #     # Perform one last check
        # if current_diff > max_diff:
        #     max_diff = current_diff
        # return max_diff
        # base case
        if not prices:
            return 0
        maximum_profit = 0 
        minimum_price = prices[0]
        # Keep track of the minimum and maxium price in a single pass 
        for price in prices[1:]:
            current_profit = price - minimum_price
            if current_profit > 0:
                # The comparison and change happen simultaneously here
                maximum_profit = max(current_profit, maximum_profit) 
            else:
                current_profit = 0
                # The comparison and change happen simultaneously here
                minimum_price = min(price, minimum_price)
        return maximum_profit

            



