class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(n ** .5) + 1)] # O(sqrt(n))
        level = [n]
        count = 0
        
        # 1->sqrt(n)->sqrt(n)^2->sqrt(n)^3->...-> O(sqrt(n)^h) = O(n^(h/2))
        while level:
            next_level = set()
            for remainder in level:
                if remainder == 0: return count
                for square in squares:
                    if remainder < square: break
                    next_level.add(remainder - square)
            count += 1
            level = next_level
        return count