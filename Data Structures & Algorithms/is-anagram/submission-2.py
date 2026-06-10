class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and all(s.count(char) == t.count(char) for char in s)