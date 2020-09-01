class Solution:
    """Determine if input s can be matched by pattern p which supports . and *."""
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def backtrack(i, j):
            if (i, j) in memo: return memo[(i, j)]  # memory

            if j == len(p) and i == len(s): return True  # criterion

            current = i < len(s) and j < len(p) and (p[j] == s[i] or p[j] == '.')  # constraint
            # choices
            if j < len(p) - 1 and p[j + 1] == '*':  # have wild card match available:
                match = any([current and backtrack(i + 1, j), backtrack(i, j + 2)])
            else:
                match = current and backtrack(i + 1, j + 1)
            memo[(i, j)] = match
            return memo[(i, j)]
            
        return backtrack(0, 0)
