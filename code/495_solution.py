class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        prev_start = prev_end = total = 0
        for t in timeSeries:
            if t > prev_end:
                total += prev_end - prev_start
                prev_start = t
            prev_end = t + duration
        total += prev_end - prev_start
        return total
            
