class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            d[t] = i