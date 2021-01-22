class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        char_freq_1, char_freq_2 = Counter(word1), Counter(word2)
        if set(char_freq_1.keys()) != set(char_freq_2.keys()): return False
        return Counter(char_freq_1.values()) == Counter(char_freq_2.values())
    
