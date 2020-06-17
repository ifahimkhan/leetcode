class Trie:
    class TrieNode:
        def __init__(self):
            self.children = collections.defaultdict(Trie.TrieNode)
            self.eow = False
        
        def __contains__(self, key): return key in self.children
        def __getitem__(self, key): return self.children[key]
        
    def __init__(self):
        self.root = Trie.TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word: node = node[char]
        node.eow = True    

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        n = len(text)
        trie = Trie()
        # O(KL) time space, K is # words, L is max len of word
        for word in words: trie.insert(word)
        
        solutions = []
        def trie_search(i):
            node = trie.root
            j = i 
            while node and j < n and text[j] in node:
                node = node[text[j]]
                if node.eow: solutions.append([i,j])
                j += 1
        
        # O(N*L)
        for i in range(n): trie_search(i)
        return solutions
