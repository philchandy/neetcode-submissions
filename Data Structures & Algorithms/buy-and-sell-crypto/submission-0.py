class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.bruteForce(prices)
    
    def bruteForce(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                profit = max((prices[j] - prices[i]), profit)
        return profit
