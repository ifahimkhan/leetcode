class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0
        len_haystack = len(haystack)
        len_needle = len(needle)
        for idx in range(len_haystack - len_needle + 1):
            if haystack[idx: idx + len_needle] == needle: return idx
        return -1
