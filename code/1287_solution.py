class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        quarter = n // 4
        candidates = [arr[quarter], arr[2 * quarter], arr[3 * quarter]]
        for candidate in candidates:
            l, h = bisect_left(arr, candidate), bisect_right(arr, candidate) - 1
            if (h - l + 1) > quarter: return candidate
        
            
