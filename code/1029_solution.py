# [10, 20], [200, 210]
# 10 + 210 == 20 + 200 
#    10         10 

# [10, 20], [10, 30], [10, 40], [10, 50]
#    10        20         30       40 
#         B                    A    
# 20 + 30 + 10 + 10
# 20 + 40 + 10 + 10
        

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])
        total = 0
        for i, cost in enumerate(costs):
            total += cost[1] if i < len(costs) // 2 else cost[0]
        return total
