class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        max_length = 0
        i = 1
        
        while i < n:
            
            while i < n and A[i-1] == A[i]: 
                i += 1
                
            up = 0
            while i < n and A[i-1] < A[i]:
                i += 1
                up += 1
            
            down = 0
            while i < n and A[i-1] > A[i]:
                i += 1
                down += 1
            
            if up and down: 
                max_length = max(max_length, up + down + 1)
                
        return max_length
