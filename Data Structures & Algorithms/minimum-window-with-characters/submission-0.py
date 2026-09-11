class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = {}

        for char in t:
            seen[char] = seen.get(char, 0) + 1
        
        required = len(set(t))
        formed = 0
        l = 0
        
        shortest_length = math.inf
        starting_pos = 0
        
        substring = {}
        for r in range(len(s)):
            if s[r] in seen:
                substring[s[r]] = substring.get(s[r], 0) + 1
                if substring[s[r]] == seen[s[r]]:
                    formed += 1 
            
            while formed == required:
                if shortest_length > r-l+1:
                    shortest_length = r-l+1
                    starting_pos = l
                if s[l] in seen:
                    if substring[s[l]] == seen[s[l]]:
                        formed -= 1
                    substring[s[l]] -= 1
                    if substring[s[l]] == 0:
                        substring.pop(s[l], None)
                l += 1
        if shortest_length == math.inf:
            return ""
        return s[starting_pos:starting_pos+shortest_length]