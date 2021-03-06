class Trie(object):
    class TrieNode(defaultdict):
        def __init__(self):
            super().__init__(Trie.TrieNode)
            self.terminal = False

    def __init__(self, words=None):
        self.root = Trie.TrieNode()
        if words: list(map(self.insert, words))

    def insert(self, word) :
        node = self.root
        for char in word: node = node[char]
        node.terminal = True


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie(map(reversed, words))
        stack = [(trie.root, 1)]
        total = 0
        while stack:
            node, depth = stack.pop()
            if node.terminal and len(node) == 0: total += depth
            else: stack.extend([(child, depth + 1) for child in node.values()])
        return total
                
