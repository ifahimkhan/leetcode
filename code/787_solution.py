# f(i,j) the cheapest price to fly from src to city j with i flights.
# f(K+1,dst) is our solution
# trans func f(i,j) = min(f(i-1,k) + price from k to j for all k)
# base case f(0,j) = INF if j != src else 0

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        INF = float('inf')
        dp = [[INF] * n for _ in range(K+2)]
        for i in range(K+2): dp[i][src] = 0

        # O(E*K)        
        for i in range(1, K+2): # O(K)
            for u, v, w in flights: # O(E)
                dp[i][v] = min(dp[i-1][u] + w , dp[i][v])
        return dp[-1][dst] if dp[-1][dst] != INF else -1
        
        
        
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        INF = float('inf')        
        # graph processing O(E) in time and space
        graph = collections.defaultdict(list)
        for u, v, w in flights: graph[u].append([v, w])
        
        # BFS search with pruning
        min_price = INF
        queue = collections.deque([[src, 0]])  # current_loc, total for the partial path
        
        # O(V^K) 
        while queue and K+2:
            for _ in range(len(queue)):
                loc, total = queue.popleft()
                if loc == dst:
                    min_price = min(min_price, total)
                else:
                    for next_, price in graph[loc]:
                        if total + price > min_price: continue
                        queue.append([next_, total + price])
            K -= 1
        return min_price if min_price != INF else -1