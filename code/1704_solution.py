class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = set('aeiouAEIOU')
        balance = 0
        for i, char in enumerate(s):
            if char in vowels:
                balance += 1 if i >= n // 2 else -1
        return balance == 0
                
