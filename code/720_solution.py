class Trie:
    class TrieNode(collections.defaultdict):
        def __init__(self):
            super().__init__(Trie.TrieNode)
            self.eow = False
    
    def __init__(self):
        self.root = Trie.TrieNode()
        self.root.eow = True
    
    def insert(self, word):
        node = self.root
        for char in word: node = node[char]
        node.eow = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words: trie.insert(word)
            
        candidate, l = [], 0
        tour = collections.deque([(trie.root, [''])])
        while tour:
            node, path = tour.pop()
            if not node.eow: continue
            if len(path) >= l:
                candidate = path
                l = len(path)
            for char in string.ascii_lowercase:
                if char in node:
                    tour.append((node[char], path + [char]))
        return ''.join(candidate)
