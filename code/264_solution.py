class Solution:
    @staticmethod
    def solution_naive_pq(n):
        factors = [2,3,5] # K
        pq = [1]
        seen = {1}
        nums = []
        for _ in range(n): # N
            num = heappop(pq) # log(NK)
            nums.append(num)
            for factor in factors:
                new_num = num * factor
                if new_num in seen: continue
                seen.add(new_num)
                heappush(pq, new_num)
        return nums[-1]
    
    @staticmethod
    def solution_tabulation(n):
        nums = [1] * n
        factors = [2,3,5]
        heads = [[0, factor] for factor in factors]
        for i in range(1, n):
            nums[i] = min(nums[i] * factor for i, factor in heads)
            for head in heads:
                if nums[head[0]] * head[1] == nums[i]: head[0] += 1
        return nums[-1]
                
    @staticmethod
    def solution_better_pq(n):
        nums = [1] * n
        factors = [2,3,5]
        pq = [[p, 1, p] for p in factors]        
        for i in range(1, n):
            nums[i] = pq[0][0]
            while nums[i] == pq[0][0]:
                t = heappop(pq)
                t[0] = nums[t[1]] * t[2]
                t[1] += 1
                heappush(pq, t)
        return nums[-1]
    
    nthUglyNumber = solution_tabulation
