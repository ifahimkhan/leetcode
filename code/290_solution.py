class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()): return False
        abbr_to_word = dict()
        word_to_abbr = dict()
        for abbr, word in zip(pattern, s.split()):
            if abbr_to_word.get(abbr, word) != word: return False
            if word_to_abbr.get(word, abbr) != abbr: return False
            abbr_to_word[abbr] = word
            word_to_abbr[word] = abbr
        return True
