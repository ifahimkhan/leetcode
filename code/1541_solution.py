class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        n_open = 0
        to_add = 0
        
        i = 0
        while i < n:
            char = s[i]
            if char == '(': 
                n_open += 1
                
            if char == ')':
                if i < n - 1 and s[i + 1] == ')':
                    i += 1
                else:
                    to_add += 1
                    
                n_open -= 1
            
            if n_open < 0:
                to_add += 1
                n_open = 0
            i += 1
        return to_add + n_open * 2
