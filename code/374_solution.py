# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            hint = guess(mid)
            if hint == 0:
                return mid
            if hint == -1:
                high = mid - 1
            if hint == 1:
                low = mid + 1
        return -1