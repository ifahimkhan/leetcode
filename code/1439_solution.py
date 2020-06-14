# 1 10 10
# 1 4  5
# 2 3  6

# smallest = first column 1+1+2 =4
# candidates for 2nd smallest:
#     1+1+3 | 1+4+2 | 10+4+3
# 2nd smallest 1+1+3 =5
# candidates
#     1+4+2 | 10+4+3 | 1+4+3 | 10+1+3 | 1+1+6
# 3rd smallest 1+4+2 = 7
#     10+4+3 | 1+4+3 | 10+1+3 | 1+5+2
    
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        nrow, ncol = len(mat), len(mat[0])
        smallest = sum(mat[i][0] for i in range(nrow))
        choice = [smallest] + [0] * nrow
        seen = set()
        pq = [choice]
        
        # O(KM^2 + KMlogMK) Time
        # O(M^2*K) space
        while k - 1: # O(K-1)
            prev = heapq.heappop(pq)
            k -= 1
            
            for i in range(nrow): # O(M)
                if prev[i+1] == ncol - 1: continue
                
                next_ = prev.copy() # O(M)
                next_[0] -= mat[i][next_[i+1]]
                next_[i+1] += 1
                next_[0] += mat[i][next_[i+1]]
                
                if tuple(next_) in seen: continue
                seen.add(tuple(next_))
                heapq.heappush(pq, next_) # (log(MK))
                
        return pq[0][0]
