class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False
        right_half = 0
        while x > right_half:
            right_half = right_half * 10 + x % 10
            x //= 10
        return right_half == x or right_half // 10 == x
