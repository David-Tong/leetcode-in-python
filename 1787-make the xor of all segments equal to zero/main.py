class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        D = 1024
        totals = [0] * L
        counts = [[0] * D for _ in range(L)]

        for x in range(k):
            for y in range(x, L, k):
                totals[x] += 1
                counts[x][nums[y]] += 1

        # print(totals)
        # print(counts)

        # helper function
        def cost(x, v):
            return totals[x] - counts[x][v]

        # process
        # dp init
        dp = [[0] * D for _ in range(L)]
        for d in range(D):
            dp[0][d] = totals[0] - counts[0][d]

        # dp transfer
        # before optimize
        """
        for x in range(k):
            for d in range(D):
                for v in range(D):
                    dp[x][d] = min(dp[x][d], dp[x-1][v^d] + cost(make set{x} all v)
        """
        # analysis
        # if v in set{x}
        """
        for x in range(k):
            for d in range(D):
                for y in range(x, L, k):
                    v = nums[y]
                    dp[x][d] = min(dp[x][d], dp[x-1][v^d] + cost(make set{x} all v)
        """
        # if v not in set{x}
        """
        for x in range(k):
            for d in range(D):
                find y s.t. dp[x-1][v] is the smallest among dp[x-1][*]
                v = d ^ y
                dp[x][d] = dp[x-1][y] + cost(make set{x} all v)
        """
        for x in range(1, k):
            mini = float("inf")
            for d in range(D):
                if dp[x - 1][d] < mini:
                    mini = dp[x - 1][d]
                    y = d

            for d in range(D):
                v = d ^ y
                dp[x][d] = dp[x - 1][y] + cost(x, v)
                for z in range(x, L, k):
                    v = nums[z]
                    dp[x][d] = min(dp[x][d], dp[x - 1][v ^ d] + cost(x, v))

        return dp[k - 1][0]


nums = [1,2,0,3,0]
k = 1

nums = [3,4,5,2,1,7,3,4,7]
k = 3

nums = [1,2,4,1,2,5,1,2,6]
k = 3

nums = [26,19,19,28,13,14,6,25,28,19,0,15,25,11]
k = 3

from random import randint
nums = [randint(0, 1023) for _ in range(2000)]
k = 1800
print(nums)


solution = Solution()
print(solution.minChanges(nums, k))
