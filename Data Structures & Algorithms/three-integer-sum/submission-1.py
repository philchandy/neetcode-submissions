class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            L = i + 1
            R = len(nums) - 1
            while L < R:
                tsum = nums[i] + nums[L] + nums[R]
                if tsum == 0 and [nums[i],nums[L],nums[R]] not in out:
                    out.append([nums[i],nums[L],nums[R]])
                    L, R = L + 1, R - 1
                elif tsum > 0:
                    R -= 1
                else:
                    L += 1
        return out

        #[-4,-1,-1,0,1,2]
    
    
    def bruteForce(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and [nums[i],nums[j],nums[k]] not in output:
                        output.append([nums[i],nums[j],nums[k]])
        return output
        