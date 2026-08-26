class Solution:
    def trap(self, height: List[int]) -> int:
        return self.twoPointers(height)

    def twoPointers(self, height: List[int]) -> int:
        maxL, maxR = 0, 0
        l,r = 0, len(height)-1
        water = 0

        while l < r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                water += maxL - max(0,height[l])
                l += 1  
            else:
                maxR = max(maxR, height[r])
                water += maxR - max(0,height[r])
                r -= 1
        return water


    def bruteForce(self, height: List[int]) -> int:
        water = 0
        
        for i in range(len(height)):
            maxL, maxR = 0, 0
            for x in range(0,i):
                maxL = max(height[x], maxL)


            for y in range(i+1, len(height)):
                maxR = max(height[y], maxR)            
            
            tallest = min(maxL, maxR)
            if tallest > height[i]:
                water += tallest - height[i]

        return water

            
            

        

        