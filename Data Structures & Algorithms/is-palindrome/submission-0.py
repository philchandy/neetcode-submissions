class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = s.lower().strip().replace(" ","")
        L,R = 0, len(s_new)-1
        while L <= R:
            if not s_new[L].isalnum():
                L += 1
                continue
            if not s_new[R].isalnum():
                R -= 1
                continue
            if s_new[L] != s_new[R]:
                return False
            L += 1
            R -= 1
        return True