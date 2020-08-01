class Solution:
    def solution_1(self, word: str) -> bool:
        upper_count = sum(map(str.isupper, word))
        return upper_count % len(word) == 0 or (upper_count == 1 and word[0].isupper())
    
    
    def solution_2(self, word):
        if word[0].isupper():
            return all(map(str.isupper, word)) or all(map(lambda x: word[x].islower(), range(1, len(word))))
        return all(map(str.islower, word))
    
    def solution_3(self, word):
        first_cap = word[0].isupper()
        c = 0
        for i, char in enumerate(word, 1):
            c += char.isupper()
            if not c: continue
            if first_cap and c in [1, i]: continue
            return False
        return True
    
    detectCapitalUse = solution_3 # solution_2 # solution_1
