# 1. use map alone
#    insert map string->val O(1)
#    sum for k in keys if k.startswith(query) then ans + val O(NL)

# 2. use prefix hash
#    insert all prefix to val mapping O(L^2) 
#    sum is now direct look up O(1)

# insert "apple" -> 3
# we do all the prefix
# "a" -> 3
# "ap" -> 3
# "app" -> 3
# "appl" -> 3
# "apple" -> 3
# insert "app" -> 2
# "a" -> 5
# "ap" -> 5
# "app" -> 5
# "appl" -> 3
# "apple" -> 3
# insert "app" -> 1
# delta 1 - 2 = -1
# "a" -> 4
# "ap" -> 4
# "app" -> 4
# "appl" -> 3
# "apple" -> 3

# 3 use Trie to have O(L) in both insert and sum

class MapSum:
    class TrieNode(collections.defaultdict):
        def __init__(self):
            super().__init__(MapSum.TrieNode)
            self.val = 0
    
    def __init__(self):
        """ Initialize your data structure here. """
        self.root = MapSum.TrieNode()
        self.map = collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map[key]
        self.map[key] = val
        node = self.root
        for char in key: 
            node = node[char]
            node.val += delta
        
    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix: 
            if char not in node: return 0
            node = node[char]
        return node.val
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)