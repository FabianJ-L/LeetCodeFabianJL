class Solution(object):
    def maxProfit(self, prices):

        lowestPrice = float('inf')
        maxPrice = 0

        for price in prices: 
            if price < lowestPrice:
                lowestPrice = price

            if price - lowestPrice > maxPrice:
                maxPrice = price - lowestPrice
            
        return maxPrice