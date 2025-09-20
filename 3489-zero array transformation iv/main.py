from distutils.command.check import check


class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        # pre-process
        N = len(nums)
        L = len(queries)

        # helper function
        # check - check if a zero array
        def check(dp):
            for x in range(N):
                if not dp[x][nums[x]]:
                    return False
            return True

        # process
        # dp init
        # dp[x][y] - if we can reach y for nums[x]
        from collections import defaultdict
        dp = [defaultdict(bool) for _ in range(N)]
        for x in range(N):
            dp[x][0] = True
        if check(dp):
            return 0

        # dp transfer
        # dp[x][y][k] = dp[x][y][k - 1] + queries[k][2]
        ans = -1
        for k in range(L):
            start, end, increase = queries[k]
            for x in range(start, end + 1):
                for y in sorted(dp[x], reverse=True):
                    dp[x][y + increase] = dp[x][y]
            # check
            if check(dp):
                ans = k + 1
                break
        return ans


nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]

nums = [4, 3, 2, 1]
queries = [[1, 3, 2], [0, 2, 1]]

nums = [1,2,3,2,1]
queries = [[0,1,1],[1,2,1],[2,3,2],[3,4,1],[4,4,1]]

nums = [1,2,3,2,6]
queries = [[0,1,1],[0,2,1],[1,4,2],[4,4,4],[3,4,1],[4,4,5]]

solution = Solution()
print(solution.minZeroArray(nums, queries))
