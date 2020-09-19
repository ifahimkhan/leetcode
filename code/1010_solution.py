class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        seen = [0] * 60
        for t in time:
            count += seen[-t % 60] 
            seen[t % 60] += 1
        return count
