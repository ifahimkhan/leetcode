class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        stoi = {s:i for i, s in enumerate('0123456789')}
        itos = {i:s for i, s in enumerate('0123456789')}
        
        def _int(x): return stoi[x]
            
        def _str(x): return itos[x]
        
        if num1 == '0' or num2 == '0': return '0'

        l1, l2 = len(num1), len(num2)
        results = [0] * (l1 + l2)

        for i, d1 in enumerate(map(_int, reversed(num1))):
            for j, d2 in enumerate(map(_int, reversed(num2))):
                carry, reminder = divmod(d1 * d2, 10)            
                results[i + j] += reminder
                results[i + j + 1] += carry

        for i, d in enumerate(results):
            carry, reminder = divmod(d, 10)
            results[i] = reminder
            if carry: results[i + 1] += carry

        return ''.join(map(_str, reversed(results))).lstrip('0')
