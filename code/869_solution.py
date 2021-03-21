class Solution:
    def __init__(self, lower_bound=1, upper_bound=10**9):
        self.answers = [Counter(str(2 ** power))
                        for power in range(
                            int(math.log2(lower_bound)),
                            int(math.log2(upper_bound)+ 1) + 1
                        )]
    
    def reorderedPowerOf2(self, N: int) -> bool:
        return Counter(str(N)) in self.answers
