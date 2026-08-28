class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minVal = prices[0]
        for i in range(len(prices)):
            if prices[i] < minVal:
                minVal = prices[i] 
            profit = max(prices[i] - minVal, profit)
        return profit

        #return self.bruteForce(prices)
    
    def bruteForce(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                profit = max((prices[j] - prices[i]), profit)
        return profit
