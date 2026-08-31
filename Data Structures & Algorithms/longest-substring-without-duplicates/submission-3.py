class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
