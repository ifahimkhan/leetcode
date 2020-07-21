# N = len(nums), M = unique number of ints in nums
# 1. elem -> freq O(N)
# 2. sort elem by freq O(MLogM) -> bubble K times O(MK) -> min PQ O(MlogK) -> quickselect O(M)
# 3. take top K O(K)


# [1,1,1,2,2,3,4,4,5,5,5,6]

# 1->3
# 5->3
# 2->2
# 4->2
# 3->1
# 6->1

#        1           2           3
#        [3,6]       [2,4]      [1,5]

# bucket sort
# 1. elem -> freq O(N)
# 2. freq -> set of elems O(M)
# 3. go over buckets and collect topk O(range(freq))

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 elem -> freq O(N)
        freq_counts = Counter(nums)
        
        # 2 freq -> set of elems O(M)
        buckets = defaultdict(set)
        for elem, freq in freq_counts.items():
            buckets[freq].add(elem)
        
        # 3 go over buckets and collect topk O(range(freq))
        topk = []
        for freq in range(len(nums), -1, -1):
            if freq in buckets: topk.extend(buckets[freq])
            if len(topk) >= k: break
        return topk[:k]
