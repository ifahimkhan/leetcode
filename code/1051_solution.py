class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # return sum(i != j for i, j in zip(heights, sorted(heights)))
        counts = [0] * 101
        for height in heights: counts[height] += 1
        
        violates, i = 0, 0
        for height in range(1, 101):
            while counts[height]:
                counts[height] -= 1
                violates += int(heights[i] != height)
                i += 1
        return violates