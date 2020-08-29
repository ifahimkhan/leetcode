# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # counter clockwise
        directions = [
            (0, 1),  # up
            (-1, 0), # left
            (0, -1), # down
            (1, 0)   # right
        ]
        visited = set()        
        
        def step_back():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
                        
        
        def dfs(x, y, d):
            robot.clean()
            visited.add((x, y))

            for _ in range(4):
                dx, dy = directions[d]
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and robot.move(): dfs(nx, ny, d)
                robot.turnLeft()
                d = (d + 1) % 4
            step_back()    
            
        dfs(0, 0, 0)
