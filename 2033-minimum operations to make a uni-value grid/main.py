class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # pre-process
        # make sure every element in the grid has some remainder when divide by x
        M = len(grid)
        N = len(grid[0])
        remainder = grid[0][0] % x
        array = list()
        for i in range(M):
            for j in range(N):
                array.append(grid[i][j])
                if grid[i][j] % x != remainder:
                    return -1

        # process
        L = len(array)
        array = sorted(array)
        middle = L // 2
        target = array[middle]
        ans = 0
        for i in range(L):
            ans += abs(array[i] - target) // x
        return ans


grid = [[2,4],[6,8]]
x = 2

grid = [[1,5],[2,3]]
x = 1

grid = [[1,2],[3,4]]
x = 2

solution = Solution()
print(solution.minOperations(grid, x))
