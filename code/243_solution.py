class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1, i2 = 0, 0
        min_dist = len(words)
        for i, word in enumerate(words, 1):
            if word == word1: i1 = i
            if word == word2: i2 = i
            if i1 and i2: min_dist = min(min_dist, abs(i1 - i2))
        return min_dist
