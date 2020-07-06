# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)


# variant 1, prefix match everytime.
class AutocompleteSystem:
    class TrieNode(defaultdict):
        def __init__(self):
            super().__init__(AutocompleteSystem.TrieNode)
            self.indices = set()
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = self.TrieNode()
        self._init_query()
        self.statistics = dict()
        self.idx_to_sentence = dict()
        for sentence, time in zip(sentences, times): self.insert(sentence, time)
    
    def _init_query(self): 
        self.query = ''
        self.trav = self.root
            
    def insert(self, sentence, time=1):
        statistics, idx_to_sentence = self.statistics, self.idx_to_sentence

        # insert or update 
        if sentence in statistics: statistics[sentence][0] += time
        else: statistics[sentence] = [time, len(statistics)]
        
        # traverse trie and annotate node with sentence idx
        i = statistics[sentence][1]
        idx_to_sentence[i] = sentence

        node = self.root
        for char in sentence: 
            node = node[char]
            node.indices.add(i)
            
    def auto_complete(self, char, k=3):
        node, statistics, idx_to_sentence = self.trav, self.statistics, self.idx_to_sentence
        # traverse
        if char not in node: return []
        node = node[char]
        
        # grab the matching sentences
        matches = []
        for i in node.indices:
            sentence = idx_to_sentence[i]
            freq = statistics[sentence][0]
            matches.append([sentence, freq])
        
        # top k query
        matches = nsmallest(k, matches, key=lambda x: [-x[1], x[0]])
        return [match[0] for match in matches]

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(self.query)
            self._init_query()
            return []
        self.query += c
        return self.auto_complete(c)

# variant 2, cache trie node. 
class AutocompleteSystem:
    class TrieNode(defaultdict):
        def __init__(self):
            super().__init__(AutocompleteSystem.TrieNode)
            self.indices = set()
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = self.TrieNode()
        self._init_query()
        self.statistics = dict()
        self.idx_to_sentence = dict()
        for sentence, time in zip(sentences, times): self.insert(sentence, time)
    
    def _init_query(self): 
        self.query = ''
        self.trav = self.root
            
    def insert(self, sentence, time=1):
        statistics, idx_to_sentence = self.statistics, self.idx_to_sentence

        # insert or update 
        if sentence in statistics: statistics[sentence][0] += time
        else: statistics[sentence] = [time, len(statistics)]
        
        # traverse trie and annotate node with sentence idx
        i = statistics[sentence][1]
        idx_to_sentence[i] = sentence

        node = self.root
        for char in sentence: 
            node = node[char]
            node.indices.add(i)
            
    def auto_complete(self, char, k=3):
        node, statistics, idx_to_sentence = self.trav, self.statistics, self.idx_to_sentence
        # traverse
        if not node or char not in node: 
            self.trav = None
            return []
        node = node[char]
        self.trav = node
        
        # grab the matching sentences
        matches = []
        for i in node.indices:
            sentence = idx_to_sentence[i]
            freq = statistics[sentence][0]
            matches.append([sentence, freq])
        
        # top k query
        matches = nsmallest(k, matches, key=lambda x: [-x[1], x[0]])
        return [match[0] for match in matches]

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(self.query)
            self._init_query()
            return []
        self.query += c
        return self.auto_complete(c)