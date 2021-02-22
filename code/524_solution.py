class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        def is_subseq(w, s):
            j = 0
            for i, c in enumerate(s):
                if c == w[j]: j += 1
                if j == len(w): return True
            return False
        
        longest_word = ''
        for w in d:
            if is_subseq(w, s):
                longest_word = min(longest_word, w, key=lambda x: (-len(x), x))
        
        return longest_word
