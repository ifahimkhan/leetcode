class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, tank, candidate = 0, 0, 0
        for i, (gain, loss) in enumerate(zip(gas, cost)):
            total += gain - loss
            tank += gain - loss
        
            if tank < 0: # reset
                tank = 0
                candidate = i + 1
        
        if total < 0: # not possible
            return -1
        return candidate 
