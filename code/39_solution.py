class Solution:
    def solution_bottom_up(self, candidates, target):
        candidates = set(candidates)
        memo = {0: [[]]}
        
        for i in range(1, target + 1):
            memo[i] = []
            for choice in candidates:
                if i - choice not in memo: continue
                memo[i].extend([candidate + [choice] 
                                for candidate in memo[i - choice] 
                                if not (candidate and choice < candidate[-1])]
                              )
        return memo[target]
    
    def solution_backtrack(self, candidates, target):
        solutions = []
        
        def _backtrack(candidate, total):
            if total > target: return
            if total == target: return solutions.append(candidate)
            
            for choice in candidates:
                if candidate and choice < candidate[-1]: continue
                _backtrack(candidate + [choice], total + choice)

        _backtrack([], 0)
        return solutions
    
    combinationSum = solution_bottom_up # solution_backtrack
