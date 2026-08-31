class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.jumpInd(s)
    def twoPointers(self, s:str) -> int:
        seen = set()
        l, r = 0, 0
        maxLength = 0

        for char in s:
            while char in seen:
                seen.remove(s[l])
                l += 1    
            r += 1
            seen.add(char)
            maxLength = max(maxLength, r-l)
        return maxLength  
    
    def jumpInd(self, s: str) -> int:
        mp = {}
        l = 0
        length = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            length = max(length, r - l + 1)
        return length
