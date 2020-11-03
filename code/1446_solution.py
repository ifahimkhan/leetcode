class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 0
        prev_char, count = s[0], 0
        for char in s:
            if char == prev_char:
                count += 1
            else:
                max_power = max(max_power, count)
                count = 1
                prev_char = char
        max_power = max(max_power, count)
        return max_power
