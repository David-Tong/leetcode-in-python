class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        N = 4

        # (x, y, d) - (x, y) with direction d in (N, E, S, W)
        status = (0, 0, 'N')
        for _ in range(N):
            for instruction in instructions:
                x, y, direction = status
                if instruction == "G":
                    if direction == 'N':
                        status = (x, y + 1, direction)
                    elif direction == 'S':
                        status = (x, y - 1, direction)
                    elif direction == 'E':
                        status = (x + 1, y, direction)
                    elif direction == 'W':
                        status = (x - 1, y, direction)
                elif instruction == "L":
                    if direction == 'N':
                        status = (x, y, 'W')
                    elif direction == 'S':
                        status = (x, y, 'E')
                    elif direction == 'E':
                        status = (x, y, 'N')
                    elif direction == 'W':
                        status = (x, y, 'S')
                elif instruction == 'R':
                    if direction == 'N':
                        status = (x, y, 'E')
                    elif direction == 'S':
                        status = (x, y, 'W')
                    elif direction == 'E':
                        status = (x, y, 'S')
                    elif direction == 'W':
                        status = (x, y, 'N')
            if status == (0, 0, 'N'):
                return True
        return False


instructions = "GGLLGG"
instructions = "GG"
instructions = "GL"
instructions = "G"
instructions = "GLLLGRRRGRRRGGGGGRR"

solution = Solution()
print(solution.isRobotBounded(instructions))
