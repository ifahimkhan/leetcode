class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse=True)
        
        max_performance = 0
        team = []
        total_speed = 0
        for e, s in engineers:
            heapq.heappush(team, s)
            total_speed += s
            while len(team) > k: total_speed -= heapq.heappop(team)
            max_performance = max(max_performance, total_speed * e)
        return max_performance % MOD
