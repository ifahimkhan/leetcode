class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ['a'] * n
        k -= n
        while k > 0:
            diff = min(25, k)
            result[n-1] = (chr(97 + diff))
            n -= 1
            k -= diff
        return ''.join(result)
