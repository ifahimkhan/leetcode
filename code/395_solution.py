class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = Counter(s)
        for c, v in counts.items():
            if v < k:
                return max([self.longestSubstring(sub, k) 
                            for sub in s.split(c) 
                            if len(sub) >= k] or [0])
        return len(s)
