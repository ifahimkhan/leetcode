class Solution:
    def calculate(self, s: str) -> int:
        stack = [(0, 1)]
        running_total, operand, sign = 0, 0, 1
        
        for c in s:
            if c.isdigit():
                operand = operand * 10 + int(c)
            elif c in '+-)':
                running_total += sign * operand
                if c == '+': sign = 1
                if c == '-': sign = -1
                if c == ')': 
                    partial, sign = stack.pop()
                    running_total = sign * running_total + partial
                operand = 0
            elif c == '(':
                stack.append((running_total, sign))
                running_total, sign = 0, 1
                
        return running_total + sign * operand
