class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.slidingWindow(s1, s2)
    
    def slidingWindow(self, s1:str, s2:str) -> bool:
        seen = {}
        for char in s1:
            seen[char] = seen.get(char, 0) + 1
        l = 0
        substring = {}
        for r in range(len(s2)):
            substring[s2[r]] = substring.get(s2[r], 0) + 1
            while r - l + 1> len(s1):
                substring[s2[l]] -= 1
                if substring[s2[l]] == 0:
                    substring.pop(s2[l], None)
                l += 1
            if substring == seen:
                return True
        return False
            

    def bruteForce(self, s1:str, s2:str) -> bool:
        seen = {}
        for char in s1:
            seen[char] = seen.get(char, 0) + 1
        
        for l in range(0,len(s2)-len(s1) + 1):
            substring = {}
            for r in range(len(s1)):
                substring[s2[r+l]] = substring.get(s2[r+l], 0) + 1
            if substring == seen:
                return True
        return False

        