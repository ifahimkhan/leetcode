class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        word_used = {beginWord}
        queue = deque([(beginWord, 1)])
        
        def get_next_word(word):
            candidates = []
            for i in range(len(word)):
                for letter in string.ascii_lowercase:
                    candidate = word[:i] + letter + word[i + 1:]
                    if candidate in wordList:
                        candidates.append(candidate)
            return candidates
        
        
        candidates = {beginWord: get_next_word(beginWord)}
        
        for word in wordList:
            candidates[word] = get_next_word(word)
            
        while queue:
            word, step = queue.popleft()
            for candidate in candidates[word]:
                if candidate == endWord: return step + 1
                if candidate in word_used: continue
                word_used.add(candidate)
                queue.append((candidate, step + 1))
            candidates[word] = []
        return 0


