class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        l = 0
        for c in s:
            if c == '(': 
                l += 1
                max_depth = max(max_depth, l)
            elif c == ')':
                l -= 1
        return max_depth
