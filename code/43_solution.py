class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        
        l1, l2 = len(num1), len(num2)
        partials = [0] * (l1 + l2)
        
        for i, d1 in enumerate(map(int, reversed(num1))):
            for j, d2 in enumerate(map(int, reversed(num2))):
                carry, reminder = divmod(d1 * d2, 10)            
                partials[i + j] += reminder
                partials[i + j + 1] += carry
        
        for i, partial in enumerate(partials):
            carry, reminder = divmod(partial, 10)
            partials[i] = reminder
            if carry: partials[i + 1] += carry
        
        return ''.join(map(str, reversed(partials))).lstrip('0')
