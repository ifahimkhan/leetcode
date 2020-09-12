class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        numbers = set(range(1, 10))
        solutions = []
        
        def backtrack(candidate, last, total):
            if len(candidate) == k and total == n: 
                return solutions.append(candidate.copy())
            if len(candidate) < k and total < n: 
                for num in range(last + 1, 10):
                    candidate.append(num)
                    total += num
                    backtrack(candidate, num, total)
                    candidate.pop()
                    total -= num
            
        backtrack([], 0, 0)
        return solutions
