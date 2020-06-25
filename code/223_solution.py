class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left = max(A, E)
        right = max(min(C, G), left)
        bottom = max(B, F)
        top = max(min(D, H), bottom)
        
        area_rec_1 = (C - A) * (D - B)
        area_rec_2 = (G - E) * (H - F)
        area_inter = (right - left) * (top - bottom)
        
        return area_rec_1 + area_rec_2 - area_inter
