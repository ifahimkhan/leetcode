class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {letter: idx for idx, letter in enumerate(order)}
        
        def lex_order(w1, w2):
            for c1, c2 in zip(w1, w2):
                if order[c1] < order[c2]: return True
                if order[c1] > order[c2]: return False
            return len(w1) <= len(w2)
        
        for w1, w2 in zip(words, words[1:]):
            if not lex_order(w1, w2): return False
        return True
        
class AlienSort:
    def __init__(self, order):
        self.order = {char: i for i, char in enumerate(order)}
        self._init_key_func()

    def _init_key_func(self):
        def lexi_order(word1, word2):
            for c1, c2 in zip(word1, word2):
                if c1 == c2: continue
                return self.order[c1] - self.order[c2]
            return len(word1) - len(word2)
        self.key_func = __import__('functools').cmp_to_key(lexi_order)
        
    def sort(self, words):
        words.sort(key=self.key_func)


if __name__ == '__main__':
    words = ["hello","leetcode", "bla", "wach", "lhhh"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    AlienSort(order).sort(words)
    print(words    
