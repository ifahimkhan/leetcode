class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        result = 0
        num_digits = 0
        for num in range(1, n+1):
            if (num & (num - 1)) == 0: num_digits += 1
            result = (result << shifts) % mod + num % mod
        return result
