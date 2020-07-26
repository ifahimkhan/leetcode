class Solution:
    @staticmethod
    def simulate(x):
        # time O(logx)
        def f(x):
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d
            return s
        
        while x >= 10: x = f(x)
            
        return x

    def experiment(self):
        # to identify pattern
        for i in range(100):
            print(i, '->', self.simulate(i))
    
    def addDigits(self, x: int) -> int:
        # constant time formula
        if not x: return 0
        return x % 9 or 9