class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.binarySearch(numbers, target)

    def bruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i < j:
                    return [i+1, j+1]
    
    def twoPointers(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while l < r:
            total = nums[l] + nums[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l+1, r+1]

    def binarySearch(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            comp = target - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == comp:
                    return [i+1, mid+1]
                elif nums[mid] > comp:
                    r = mid -1
                else:
                    l = mid + 1
        return []