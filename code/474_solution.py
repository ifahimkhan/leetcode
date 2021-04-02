# bottm up DP

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}
        
        for s in strs:
            n0, n1 = s.count('0'), s.count('1')
            
            update = dict()
            for (u0, u1), v in dp.items(): 
                # try to add string to all the existing subsets
                if u0 + n0 > m or u1 + n1 > n: continue
                update[(u0 + n0, u1 + n1)] = max(1 + v, dp.get((u0 + n0, u1 + n1), 0))
            dp.update(update)
            
        return max(dp.values())                    
                    
                                
