class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        M = len(wall)
        N = sum(wall[0])

        from collections import defaultdict
        bricks = defaultdict(int)
        for row in wall:
            total = 0
            for brick in row:
                total += brick
                if total != N:
                    bricks[total] += 1

        if len(bricks) > 0:
            return M - max(bricks.values())
        else:
            return M


wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
wall = [[1],[1],[1]]
wall = [[3]]

solution = Solution()
print(solution.leastBricks(wall))
