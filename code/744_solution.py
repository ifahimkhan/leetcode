class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, h = 0, len(letters)
        while l < h:
            m = (h + l) // 2
            if letters[m] <= target: l = m + 1
            else: h = m
        return letters[l % len(letters)]
