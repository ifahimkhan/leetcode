class Solution:
    def sort_binary_search(self, intervals):
        # O(N) space O(NlogN) time
        starts_indices = [(float('inf'), -1)]
        for i, (l, r) in enumerate(intervals):
            starts_indices.append((l, i))
        starts_indices.sort()
        
        # O(NlogN)
        results = []
        for l, r in intervals: # O(N) outer loop
            i = bisect_left(starts_indices, (r, -1))
            results.append(starts_indices[i][1]) # O(logN) binary search inner
        return results        
    
    def two_arrays_with_map(self, intervals):
        n = len(intervals)
        
        # O(N) time / space
        itv_to_idx = {tuple(itv): i for i, itv in enumerate(intervals)}
        
        # O(N) time / space
        end_intervals = intervals.copy()
        
        # O(NlogN)
        intervals.sort()
        end_intervals.sort(key = lambda x: x[1])

        j = 0
        results = [-1] * n
        # O(N) construct results
        for i, itv in enumerate(end_intervals): # O(N) outer loop
            while j < n and intervals[j][0] < itv[1]: j += 1 # O(N) in total
            if j < n: results[itv_to_idx[tuple(itv)]] = itv_to_idx[tuple(intervals[j])]
        return results

    findRightInterval = two_arrays_with_map # sort_binary_search
