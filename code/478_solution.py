class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
    
    def randPoint(self) -> List[float]:  
        x_center, y_center, radius = self.x_center, self.y_center, self.radius
        while True:
            x = random.uniform(x_center - radius, x_center + radius)
            y = random.uniform(y_center - radius, y_center + radius)
            if (x - x_center) ** 2 + (y - y_center) ** 2 <= radius ** 2:
                return [x, y]
            
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
