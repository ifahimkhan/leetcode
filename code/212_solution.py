class Trie:
    class TrieNode(collections.defaultdict):
        def __init__(self):
            super().__init__(Trie.TrieNode)
            self.word = ""
            
    def __init__(self):
        self.root = Trie.TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word: node = node[char]
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        nrow, ncol = len(board), len(board[0])
        
        trie = Trie()
        for word in words: trie.insert(word)
        
        crossed = set()
        def backtrack(node, r, c):
            if node.word: crossed.add(node.word)
            
            if 0 <= r < nrow and 0 <= c < ncol and board[r][c] in node:
                char = board[r][c]
                board[r][c] = 'X'
                for rr, cc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    backtrack(node[char], rr, cc)
                board[r][c] = char
        
        for r in range(nrow):
            for c in range(ncol):
                backtrack(trie.root, r, c)
        return crossed
