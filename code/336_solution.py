class Solution:
    class TrieNode(collections.defaultdict):
        def __init__(self):
            super().__init__(Solution.TrieNode)
            self.word_idx = -1
            self.list = []
                
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def partial_palindrome(w, l):
            r = len(w) - 1
            while l < r:
                if w[l] != w[r]: return False
                l += 1
                r -= 1
            return True
        
        # populating the trie
        root = Solution.TrieNode()
        for i, word in enumerate(words):
            node = root
            reversed_word = word[::-1] 
            for j, char in enumerate(reversed_word):
                if partial_palindrome(reversed_word, j): node.list.append(i)
            # for j, char in enumerate(word):
                # if partial_palindrome(word, j): node.list.append(i)
                node = node[char]    
            node.word_idx = i
        
        pairs = []
        # find the pairs
        for i, word in enumerate(words):
            node = root
            for j, char in enumerate(word):                
            # reversed_word = word[::-1]
            # for j, char in enumerate(reversed_word):
                # case 3: word[j] is longer than a possible word[i]
                if node.word_idx != -1 and partial_palindrome(word, j): pairs.append([i, node.word_idx])                    
                # if node.word_idx != -1 and partial_palindrome(reversed_word, j): pairs.append([node.word_idx, i])
                if char not in node: break
                node = node[char]
            else:
                # case 1: word[i] == word[j][::-1]
                if node.word_idx not in [-1, i]: pairs.append([i, node.word_idx])
                # if node.word_idx not in [-1, i]: pairs.append([node.word_idx, i])  
                # case 2: word[i] is abc|sos  word[j]  cba
                for k in node.list: pairs.append([i, k]) 
                # for k in node.list: pairs.append([k, i])   
                    
        return pairs    

    
class TrieNode(defaultdict):
    def __init__(self):
        super().__init__(TrieNode)
        self.word_idx = -1
        self.list = []


class Solution:
    def solution_trie_lazy(self, words: List[str]) -> List[List[int]]:
        def partial_palindrome(w, l):
            r = len(w) - 1
            while l < r:
                if w[l] != w[r]: return False
                l += 1; r -= 1
            return True
        
        def dfs_gather(node):
            partial_palindrome_list = []
            stack = [(child, [char]) for char, child in node.items()]
            while stack:
                node, seqs = stack.pop()
                if node.word_idx != -1 and partial_palindrome(seqs, 0): partial_palindrome_list.append(node.word_idx)
                stack.extend([(child, seqs + [char]) for char, child in node.items()])
            return partial_palindrome_list
            
        # populating the trie
        root = TrieNode()
        for i, word in enumerate(words):
            node = root
            for char in reversed(word): node = node[char]
            node.word_idx = i
        
        pairs = []
        # find the pairs
        for i, word in enumerate(words):
            node = root
            for j, char in enumerate(word):                
                # case 3: word[j] is longer than a possible word[i]
                if node.word_idx != -1 and partial_palindrome(word, j): pairs.append([i, node.word_idx])                    
                if char not in node: break
                node = node[char]
            else:
                # case 1: word[i] == word[j][::-1]
                if node.word_idx not in [-1, i]: pairs.append([i, node.word_idx])
                # case 2: word[i] is abc|sos  word[j]  cba
                node.list = dfs_gather(node)
                for k in node.list: pairs.append([i, k])
        return pairs    
                
    
    palindromePairs = solution_trie_lazy 
