class Solution:
    def reorderSpaces(self, text: str) -> str:
        n_spaces = text.count(' ')
        words = text.split()
        n_words = len(words)
        
        if n_spaces == 0 or n_words == 1: 
            return ''.join(words) + ' ' * n_spaces
        
        result = []
        gap, tail = divmod(n_spaces, n_words - 1)
        for i, word in enumerate(words[:-1]):
            result.extend([word, ' ' * gap])
        result.extend([words[-1], ' ' * tail])
        return ''.join(result)
