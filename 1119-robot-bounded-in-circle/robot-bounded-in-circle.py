class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        x , y = 0, 0
        direction_idx = 0
        for i in instructions:
            if i == 'G': 
                dx, dy = directions[direction_idx]
                x += dx
                y += dy
            elif i == 'L':
                direction_idx = (direction_idx - 1) % 4
            elif i == 'R':
                direction_idx = (direction_idx + 1) % 4
        
        return (x == 0 and y == 0) or direction_idx != 0


        