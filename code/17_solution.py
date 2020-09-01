class Solution:
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        n = len(digits)
        solutions = []
        
        def dfs(candidate, idx):
            if idx == n: return solutions.append(candidate)
            for char in self.mapping[digits[idx]]:
                dfs(candidate + char, idx + 1)

        dfs('', 0)
        return solutions
