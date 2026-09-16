class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        dq = deque()
        closing = [')', ']', '}']
        for char in s:
            if char in closing:
                if len(dq) == 0:
                    return False 
                out = dq.pop()
                if pairs[out] != char:
                    return False
                continue
            dq.append(char)
        if len(dq) == 0:
            return True
        else:
            return False