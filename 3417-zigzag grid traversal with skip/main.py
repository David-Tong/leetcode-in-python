class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        # process
        ans = list()
        idx_x = 0
        while idx_x < M:
            if idx_x % 2 == 0:
                idx_y = 0
                while idx_y < N:
                    ans.append(grid[idx_x][idx_y])
                    idx_y += 2
            else:
                if N % 2 == 0:
                    idx_y = N - 1
                else:
                    idx_y = N - 2
                while idx_y >= 0:
                    ans.append(grid[idx_x][idx_y])
                    idx_y -= 2
            idx_x += 1
        return ans


grid = [[1,2],[3,4]]
grid = [[2,1],[2,1],[2,1]]
grid = [[1,2,3],[4,5,6],[7,8,9]]

solution = Solution()
print(solution.zigzagTraversal(grid))
