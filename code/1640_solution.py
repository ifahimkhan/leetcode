class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        initials = {p[0]: p for p in pieces}
        
        l = 0
        while l < n:
            if arr[l] not in initials: return False
            piece = initials[arr[l]]
            for c in piece:
                if l >= n or c != arr[l]: return False
                l += 1
        return True
