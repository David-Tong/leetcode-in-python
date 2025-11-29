class Solution(object):
    def checkValidGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        from collections import defaultdict
        dicts = defaultdict(tuple)
        for x in range(M):
            for y in range(N):
                dicts[grid[x][y]] = (x, y)
        # print(dicts)

        # helper function
        def validMove(start, end):
            start_x, start_y = start
            end_x, end_y = end
            if abs(start_x - end_x) == 1:
                return abs(start_y - end_y) == 2
            elif abs(start_x - end_x) == 2:
                return abs(start_y - end_y) == 1
            else:
                return False

        # process
        if grid[0][0] != 0:
            return False

        idx = 1
        while idx < M * N:
            if not validMove(dicts[idx - 1], dicts[idx]):
                return False
            idx += 1
        return True


grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
grid = [[0,3,6],[5,8,1],[2,7,4]]
grid = [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]

solution = Solution()
print(solution.checkValidGrid(grid))
