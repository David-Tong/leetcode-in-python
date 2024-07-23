class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        # pre-process
        L = len(positions)
        robots = list()
        for x in range(L):
            robots.append([positions[x], healths[x], directions[x], x])
        robots = sorted(robots, key=lambda x: x[0])

        # process
        stack = list()
        for x in range(L):
            if robots[x][2] == "R":
                stack.append(robots[x])
            else:
                # only collide with R direction robots
                while stack and stack[-1][2] == "R":
                    # coming robot with lower health
                    if stack[-1][1] > robots[x][1]:
                        robots[x][1] = 0
                        stack[-1][1] -= 1
                        break
                    # coming robot with same health
                    elif stack[-1][1] == robots[x][1]:
                        stack.pop()
                        robots[x][1] = 0
                        break
                    # coming robot with higher health
                    else:
                        stack.pop()
                        robots[x][1] -= 1

                if robots[x][1] > 0:
                    stack.append(robots[x])

        # post-process
        stack = sorted(stack, key=lambda x: x[3])
        ans = [x[1] for x in stack]
        return ans


positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"

positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"

positions = [1,2,5,6]
healths = [10,10,11,11]
directions = "RLRL"

positions = [3,5,2,6]
healths = [10,10,2,1]
directions = "RLRL"

positions = [3,40]
healths = [49,11]
directions = "LL"

solution = Solution()
print(solution.survivedRobotsHealths(positions, healths, directions))
