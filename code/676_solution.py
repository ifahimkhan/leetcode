class MagicDictionary:
    def _gen_neighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i + 1:]
    
    def buildDict(self, words) -> None:
        """Build a dictionary through a list of words."""
        self.words = set(words)
        self.neighbor_counts = collections.defaultdict(int)
        for word in words:
            for neighbor in self._gen_neighbors(word):
                self.neighbor_counts[neighbor] += 1
            
        
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        counts = sum(map(self.neighbor_counts.__getitem__, self._gen_neighbors(word)))
        if word in self.words: 
            return counts > len(word)
        return counts >= 1

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
