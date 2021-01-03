class Solution:
    def countArrangement(self, n: int) -> int:
        count = [0]
        options = {num: 1 for num in range(1, n + 1)}
        
        def backtrack(i):
            if i > n: count[0] += 1            
            for option, available in options.items():
                if not available: continue
                if i % option == 0 or option % i == 0:
                    options[option] = 0
                    backtrack(i + 1)
                    options[option] = 1
        
        backtrack(1)
        return count[0]
