class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                break
        else:
            return arr
        
        r_max = arr[i + 1]
        r_max_idx = i + 1
        for j in range(i + 2, n):
            if arr[i] > arr[j] > r_max:
                r_max = arr[j]
                r_max_idx = j
        
        arr[i], arr[r_max_idx] = arr[r_max_idx], arr[i]
        return arr
            
