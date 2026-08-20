class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return self.twoPointers(heights)
    
    def bruteForce(self, heights: List[int]) -> int:
        maxSize = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                curr = (j-i) * min(heights[i],heights[j])
                maxSize = max(curr, maxSize)
        return maxSize

    def twoPointers(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        maxSize = 0
        while L < R:
            curr = (R-L) * min(heights[L], heights[R])
            maxSize = max(curr, maxSize)
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return maxSize
