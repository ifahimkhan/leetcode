class Solution:
    def solution_linear_search(self, arr: List[int]) -> int:
        diff1, diff2 = arr[1] - arr[0], arr[~0] - arr[~1]
        diff = sorted([diff1, diff2], key=abs)[0]
        for a1, a2 in zip(arr, arr[1:]):
            if a2 - a1 != diff:
                return a1 + diff
        return arr[0]    
    
    def solution_binary_search(self, arr):
        n = len(arr)
        diff = (arr[~0] - arr[0]) // n
        
        l, h = 0, n - 1
        while l < h:
            m = (l + h) // 2
            if arr[m] == arr[0] + m * diff: 
                l = m + 1
            else:
                h = m
        return arr[0] + l * diff
    
    missingNumber = solution_binary_search # solution_linear_search
