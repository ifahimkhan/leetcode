class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.translate(str.maketrans("!?',;.", "      ")).lower()
        banned = set(banned)
        word_freq = defaultdict(int)
        most_freq_word, max_freq = '', 0
        for word in paragraph.split():
            if word in banned: continue
            word_freq[word] += 1
            if word_freq[word] > max_freq:
                most_freq_word, max_freq = word, word_freq[word]
        return most_freq_word
