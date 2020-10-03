class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freqs = Counter(nums)
        total = 0
        for num in freqs:
            if (k == 0 and freqs[num] > 1) or (k > 0 and num + k in freqs):
                total += 1
        return total
