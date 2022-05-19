class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.M = len(grid)
        self.N = len(grid[0])

        def doSwim(grid, k):
            if grid[0][0] > k or grid[self.M - 1][self.N - 1] > k:
                return False

            from collections import deque
            bfs = deque()
            bfs.append((0, 0))
            visit = set()
            visit.add((0, 0))
            while bfs:
                cx, cy = bfs.popleft()
                for dx, dy in self.DIRECTIONS:
                    nx = cx + dx
                    ny = cy + dy
                    if 0 <= nx < self.M and 0 <= ny < self.N:
                        if grid[nx][ny] <= k:
                            if nx == self.M - 1 and ny == self.N - 1:
                                return True
                            if (nx, ny) not in visit:
                                bfs.append((nx, ny))
                                visit.add((nx, ny))
            return False

        if self.M == self.N == 1:
            return grid[0][0]

        left = 0
        right = 0
        for row in grid:
            for item in row:
                right = max(right, item)

        while left + 1 < right:
            middle = (left + right) // 2
            if doSwim(grid, middle):
                right = middle - 1
            else:
                left = middle + 1

        if doSwim(grid, left):
            return left
        elif doSwim(grid, right):
            return right
        else:
            return right + 1


grid = [[0,2],[1,3]]
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
grid = [[0]]

solution = Solution()
print(solution.swimInWater(grid))
