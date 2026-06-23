class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(len(nums) -1):
            prefix[i+1] = prefix[i] * nums[i]
        suffix = [1] * len(nums)
        for i in range(len(nums)-1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]
        return [x * y for x,y in zip(prefix, suffix)]