class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0: return '0'
        results = deque()
        d = 0
        while n:
            d += 1
            n, digit = divmod(n, 10)
            results.appendleft(str(digit))
            if d == 3 and n: results.appendleft('.')
            d %= 3
        return ''.join(results)