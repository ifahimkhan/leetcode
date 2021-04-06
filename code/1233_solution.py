class Trie(object):
    class TrieNode:
        def __init__(self):
            self.sub_directories = defaultdict(Trie.TrieNode)
            self.terminal = False

    def __init__(self):
        self.root = self.TrieNode()

    def add(self, directory):
        trie = self.root
        for level in directory.split('/'):
            trie = trie.sub_directories[level]
            if trie.terminal: return # add this line too speed up
        trie.terminal = True


class Solution:
    def removeSubfolders(self, directories: List[str]) -> List[str]:        
        trie = Trie()
        for directory in directories:
            trie.add(directory)
        
        pruned_directories = []
        stack = [(trie.root, [])]
        while stack:
            directory, dirname = stack.pop()
            if directory.terminal:
                pruned_directories.append('/'.join(dirname))
                continue
            for level, sub_directory in directory.sub_directories.items():
                stack.append([sub_directory, dirname + [level]])
        
        return pruned_directories
