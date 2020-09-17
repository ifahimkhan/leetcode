class Solution:
    # At the end of one pass of instructions. the robot moved a in x, b in y
    # 1. if a == 0 and b == 0, it went back to origin thus a cycle in one pass of instruction
    # 2. if a != 0 or b != 0
    #    a. it is facing the same starting direction.
    #       - then the more pass of instructions we do the farther it went. 
    #    b. it is facing another direction
    #       - work with a few example to show it will eventually go back to origin.
    
    def isRobotBounded(self, instructions: str) -> bool:
        # there are better ways to do direction changes, but might be too hard for interview
        dirs = {'n': (0, 1), 'e': (1, 0), 's': (0, -1), 'w': (-1, 0)}
        turn_right = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
        turn_left = {'n': 'w', 'w': 's', 's': 'e', 'e': 'n'}
        x, y, d = 0, 0, 'n'
        for i in instructions:
            if i == 'R': d = turn_right[d]
            elif i == 'L': d = turn_left[d]
            else: x, y = x + dirs[d][0], y + dirs[d][1]
        return x == y == 0 or d != 'n' 
