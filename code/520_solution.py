class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper_count = sum(map(str.isupper, word))
        return (upper_count % len(word) == 0) or (upper_count == 1 and word[0].isupper())