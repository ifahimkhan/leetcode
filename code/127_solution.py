class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        word_used = {beginWord}
        
        def get_next_word(word):
            for i in range(len(word)):
                for letter in string.ascii_lowercase:
                    next_word = word[:i] + letter + word[i + 1:]
                    if next_word in wordList and next_word not in word_used:
                        yield next_word

        queue = deque([(beginWord, 1)])
        while queue:
            word, step = queue.popleft()
            for next_word in get_next_word(word):
                if next_word == endWord: return step + 1
                word_used.add(next_word)
                queue.append((next_word, step + 1))
        return 0
