class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        # Define coordinates for North, East, South, West
        directions = [(0,1), (1,0), (0,-1), (-1, 0)]

        obstacle = set(map(tuple, obstacles))

        x, y, direction = 0, 0, 0
        max_distance = 0
        
        # FOR : To evaluate each step taken
        for step in commands:
            # CONDITION : To turn right
            if step == -1:
                # Increment value by 1, if facing N (0,1), turn right, we face East (1,1)
                # % : To keep the value in given range, i.e., 4, so max could be (0,3)
                direction = (direction + 1) % 4
            
            # CONDITION : To turn left
            elif step == -2:
                # Increment value by 3, since it turns anticlockwise
                # % : To keep the value in given range, i.e., 4, so max could be (0,3)
                direction = (direction + 3) % 4

            # CONDITION: If robot moves forward
            else:
                # FOR : For i steps
                for i in range(step):
                    # Assume the robot is at position (0, 0) & facing N (direction = 0)
                    # It receives command to move forward 1 step
                    # directions[0] = (0, 1); i.e. directions[0][0] = 0, directions[0][1] = 1
                    new_x, new_y = x + directions[direction][0], y + directions[direction][1]

                    # CONDITION 
                    if (new_x, new_y) not in obstacle:
                        x, y = new_x, new_y
                        max_distance = max(max_distance, x*x + y*y)
                    else:
                        break
        return max_distance
        
