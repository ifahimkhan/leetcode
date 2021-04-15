class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        total = sum(data)
        min_swaps = total
        ones_in_window = 0

        l, r = 0, 0
        while r < n:
            ones_in_window += data[r]
            r += 1
            
            if r - l > total:
                ones_in_window -= data[l]
                l += 1
            
            min_swaps = min(min_swaps, total - ones_in_window)
        
        return min_swaps
        
