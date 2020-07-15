class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour % 12 + minutes / 60) * 30
        m = minutes * 6
        angle = abs(m - h)
        return min(angle, 360 - angle)