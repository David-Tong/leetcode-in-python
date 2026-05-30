class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        # process
        from copy import deepcopy
        ans = deepcopy(grid)
        for dx in range(k):
            sx = x + dx
            tx = x + k - 1 - dx
            if sx != tx:
                for sy in range(y, y + k):
                    ans[sx][sy] = grid[tx][sy]
        return ans


grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
x = 1
y = 0
k = 3

"""
grid = [[3,4,2,3],[2,3,4,2]]
x = 0
y = 2
k = 2
"""

solution = Solution()
print(solution.reverseSubmatrix(grid, x, y, k))
