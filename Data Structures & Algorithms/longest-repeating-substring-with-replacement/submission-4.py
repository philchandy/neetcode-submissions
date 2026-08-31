class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return self.slidingWindow(s, k)

    def bruteForce(self, s: str, k: int) -> int:
        maxLength = 0
        
        for l in range(len(s)):
            mp = {}
            maxFreq = 0
            for r in range(l, len(s)):
                mp[s[r]] = 1 + mp.get(s[r], 0)
                maxFreq = max(maxFreq, mp[s[r]])
                substringLength = r - l + 1
                replacements = substringLength - maxFreq

                if replacements <= k:
                    maxLength = max(substringLength, maxLength)
        return maxLength
        
    def slidingWindow(self, s:str, k:int) -> int:
        maxLength = 0
        l = 0
        mp = {}
        maxFreq = 0
        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxFreq = max(maxFreq, mp[s[r]])
            
            while ((r-l+1) - maxFreq > k):
                mp[s[l]] = mp.get(s[l]) - 1
                l += 1
            maxLength = max(maxLength, r-l+1)
        return maxLength
        