class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        dq = deque()
        maxlist = []
        for r in range(len(nums)):
            while len(dq)>0 and nums[r] > nums[dq[len(dq)-1]]:
                dq.pop()
            dq.append(r)
            if dq[0] < l:
                dq.popleft()
            if r-l+1 == k:
                maxlist.append(nums[dq[0]])
                l += 1
        return maxlist

        

    def bruteForce(self, nums: List[int], k: int) -> List[int]:
        res = []
        for l in range(len(nums)-k+1):
            mx = nums[l]
            for r in range(l, l+k):
                mx = max(mx, nums[r])
            res.append(mx)
        return res