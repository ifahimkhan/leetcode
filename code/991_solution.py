class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y < X: return X - Y
        
        steps = 0
        while X < Y:
            if Y & 1:
                Y += 1
            else:
                Y >>= 1
            steps += 1
        return steps + X - Y
