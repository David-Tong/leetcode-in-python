class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        L = len(grid)
        nums = [0] * (L * L + 1)

        # process
        for x in range(L):
            for y in range(L):
                nums[grid[x][y]] += 1

        repeated, missing = 0, 0
        for x in range(1, L * L + 1):
            if nums[x] == 0:
                missing = x
            elif nums[x] == 2:
                repeated = x
        ans = [repeated, missing]
        return ans


grid = [[1,3],[2,2]]
grid = [[9,1,7],[8,9,2],[3,4,6]]

solution = Solution()
print(solution.findMissingAndRepeatedValues(grid))
