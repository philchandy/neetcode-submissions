class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = list(set(nums))
        return False if len(unique_set) == len(nums) else True
        