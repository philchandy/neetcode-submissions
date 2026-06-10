class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cp = list(s)
        s_cp.sort()
        t_cp = list(t)
        t_cp.sort()
        return  s_cp == t_cp 