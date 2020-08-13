class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        results, min_sum = [], float('inf')
        r_to_idx = dict()
        for i, r in enumerate(list1): r_to_idx[r] = i
        for i, r in enumerate(list2): 
            if r not in r_to_idx: continue
            indices_sum = i + r_to_idx[r]
            if indices_sum < min_sum:
                min_sum = indices_sum
                results = [r]
            elif indices_sum == min_sum:
                results.append(r)
        return results
