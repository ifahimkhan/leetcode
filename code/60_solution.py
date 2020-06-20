class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        factorial = [1]
        for i in range(1, n): factorial.append(factorial[-1] * i)
        
        k -= 1
        digits = list(map(str, range(1, n+1)))
        result = []
        while n:
            i, k = divmod(k, factorial[n-1])
            result.append(digits.pop(i))     
            n -= 1
        return ''.join(result)