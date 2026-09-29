class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operands = set(("+", "-", "*", "/"))
        
        for char in tokens:
            if char in operands:
                j = stack.pop()
                out = stack.pop()
                if char == '+':
                    out = out + j
                elif char == '-':
                    out = out - j
                elif char == '*':
                    out = out * j 
                else:
                    out = int(out / j)
                stack.append(out)
            else:
                stack.append(int(char))
        return stack.pop()