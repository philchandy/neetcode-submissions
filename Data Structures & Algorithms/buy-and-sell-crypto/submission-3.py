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

    def twoPointers(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit
    
    def bruteForce(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                profit = max((prices[j] - prices[i]), profit)
        return profit
