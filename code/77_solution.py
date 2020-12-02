class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solutions = []
        
        def backtrack(candidate, choices, num_choice):
            if not choices or not num_choice:
                solutions.append(candidate)
                return
            
            for i, choice in enumerate(choices, 1):
                if len(choices[i:]) < num_choice - 1: continue
                backtrack(candidate + [choice], choices[i:], num_choice - 1)
                
        backtrack([], range(1, n + 1), k)
        return solutions
            
                
            
