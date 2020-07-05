class Trie:
    class TrieNode(defaultdict):
        def __init__(self):
            super().__init__(Trie.TrieNode)
            self.word_indices = []
    
    def __init__(self, words=[]):
        self.root = Trie.TrieNode()
        self.words = []
        for word in words: self.insert(word)
        
    def insert(self, word, i=None):
        if not i: i = len(self.words)
        self.words.append(word)
        node = self.root
        for char in word: 
            node = node[char]
            node.word_indices.append(i)

    def prefix_match(self, prefix):
        if not prefix: return self.words
        node = self.root
        for char in prefix:
            if char not in node: return []
            node = node[char]
        return [self.words[i] for i in node.word_indices]
        
        
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie(words)
        squares = []
        
        def backtrack(candidate, step):
            if candidate and len(candidate) == len(candidate[0]): 
                return squares.append(candidate.copy())            
                
            prefix = ''.join(word[step] for word in candidate)
            for word in trie.prefix_match(prefix):
                candidate.append(word)
                backtrack(candidate, step + 1)
                candidate.pop()
        
        backtrack([], 0)            
        return squares
