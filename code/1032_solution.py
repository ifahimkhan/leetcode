class StreamChecker:
    class TrieNode(collections.defaultdict):
        def __init__(self):
            super().__init__(StreamChecker.TrieNode)
            self.eow = False

    def __init__(self, words: List[str]):
        self.trie = StreamChecker.TrieNode()
        self.stream = deque()
        for word in set(words):
            node = self.trie
            for char in reversed(word): node = node[char]
            node.eow = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for char in self.stream:
            if node.eow: return True
            if char not in node: return False
            node = node[char]
        return node.eow


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)