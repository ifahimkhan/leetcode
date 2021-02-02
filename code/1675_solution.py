class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = [[num // (num & -num), num] for num in nums]
        heapify(pq)
        res = float('inf')
        
        ma = max(a for a, _ in pq)
        
        while len(pq) == len(nums):
            a, a0 = heapq.heappop(pq)
            res = min(res, ma - a)
            if a % 2 == 1 or a < a0:
                ma = max(ma, a * 2)
                heappush(pq, [a * 2, a0])
        return res
