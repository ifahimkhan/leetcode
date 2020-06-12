class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # pq = [1]
        # seen = {1}
        # # loose upper bound O(NKlog(NK))
        # while n: # O(N)
        #     num = heapq.heappop(pq) #O(log(S))
        #     if n == 1: return num 
        #     for prime in primes: #O(K)
        #         new_num = num * prime
        #         if new_num in seen: continue
        #         heapq.heappush(pq, new_num) #O(log(S))
        #         seen.add(new_num)
        #     n -= 1
        
        # # loose upper bound O(NKlog(K))
        ugly_number = [1]
        pq = [[p, 0, p] for p in primes]
        while n - 1: #(N)
            num = pq[0][0]
            ugly_number.append(num)
            while pq[0][0] == num: # O(K)
                t = heapq.heappop(pq) # O(log(K))
                t[1] += 1
                t[0] = ugly_number[t[1]] * t[2] 
                heapq.heappush(pq, t)
            n -= 1
        return ugly_number[-1]