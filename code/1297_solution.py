class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        substring_freq = dict()
        for i in range(n - minSize + 1):
            substring = s[i: i+minSize]
            if len(set(substring)) > maxLetters: continue
            substring_freq[substring] = substring_freq.get(substring, 0) + 1
        return 0 if not substring_freq else max(substring_freq.values())
