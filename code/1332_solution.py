class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        
        def is_palindrome(s):
            l, h = 0, len(s) - 1
            while h > l:
                if s[l] != s[h]: return False
                l += 1
                h -= 1
            return True
        
        return 1 if is_palindrome(s) else 2
