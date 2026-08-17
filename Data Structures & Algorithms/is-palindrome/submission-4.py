class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(char.lower() for char in s if char.isalnum())
        return t == t[::-1]