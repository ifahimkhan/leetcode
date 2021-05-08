class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n_b, n_w = len(boxes), len(warehouse)
        
        boxes.sort()
        
        prev_min = warehouse[0]
        for w_i, wh in enumerate(warehouse):
            prev_min = min(prev_min, wh)
            warehouse[w_i] = prev_min
        
        total = 0
        b_i, w_i = 0, n_w - 1
        while b_i < n_b and w_i >= 0:
            if boxes[b_i] <= warehouse[w_i]:
                total += 1
                b_i += 1
            w_i -= 1
        return total
        
            
