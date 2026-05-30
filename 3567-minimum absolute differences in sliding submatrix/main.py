class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        def patch(xs, ys):
            nums = set()
            for x in range(xs, min(M, xs + k)):
                for y in range(ys, min(N, ys + k)):
                    nums.add(grid[x][y])
            if len(nums) == 1:
                return 0
            nums = sorted(nums)
            idx = 0
            res = float("inf")
            while idx < len(nums) - 1:
                res = min(res, abs(nums[idx + 1] - nums[idx]))
                idx += 1
            return res

        # process
        ans = [[0] * (N - k + 1) for _ in range(M - k + 1)]
        for x in range(M - k + 1):
            for y in range(N - k + 1):
                ans[x][y] = patch(x, y)
        return ans


grid = [[1,8],[3,-2]]
k = 2

grid = [[3,-1]]
k = 1

grid = [[1,-2,3],[2,3,5]]
k = 2

grid = [[3,3,3],[3,3,3]]
k = 2

solution = Solution()
print(solution.minAbsDiff(grid, k))
