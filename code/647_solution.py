class Solution:
    def countSubstrings(self, s: str) -> int:
        total, n = 0, len(s)
        
        for i in range(n):
            for j in [0, 1]:
                left, right = i, left + j

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    total += 1
                    left -= 1
                    right += 1
        return total
