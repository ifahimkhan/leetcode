---
title: Trie  
author: Ren Zhang
date: June-15-2020
---  

# Trie | Prefix Tree  
![trie](./assets/Trie.png)

## Remarks 
+ Trie (pronounce as try) is a N-way tree used to store and facilitate (prefix)search of string valued keys.
+ The node path corresponds to the characters in the key. 
+ The basic operations on trie like *insert*, *get* or prefix search *has_prefix* all take linear time $$O(L)$$ wrt length of the search term.
+ Given a prefix, we can first find if the prefix is in Trie and then from the node corresponding to the last characters in prefix, we can do a DFS search on trie to find all words with that prefix. 
+ Each node can hold more information than just the link and flag, difficult question may require us to precompute some results to set to the nodes during the insert.  
+ Finally, most questions solvable with Trie can also be solved with prefix hashing, there are trade offs we need to consider when comparing these two approaches. 

## Implementation
```python
class Trie(object):
    class TrieNode(collections.defaultdict):
        def __init__(self):
            super().__init__(Trie.TrieNode)
            self.word = ""

    def __init__(self, words=None):
        self.root = Trie.TrieNode()
        if words: list(map(self.insert, words))

    def insert(self, word) :
        node = self.root
        for char in word: node = node[char]
        node.word = word

    def _get(self, word):
        node = self.root
        for char in word:
            if char not in node: return None
            node = node[char]
        return node

    def __contains__(self, word):
        node = self._get(word)
        return node is not None and node.word

    def has_prefix(self, prefix):
        return self._get(prefix) is not None

    def startswith(self, prefix):
        node = self._get(prefix)
        stack = [node]
        words = []
        while stack: # DFS search
            node = stack.pop()
            if node.word: words.append(node.word)
            stack.extend(node.values())
        return words
```

