class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.twoPointers(s)

    def stringManipulation(self, s: str) -> bool:
        t = "".join(char.lower() for char in s if char.isalnum())
        return t == t[::-1]

    def twoPointers(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True