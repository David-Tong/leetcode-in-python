class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        # process
        # dp init
        # dp[x][y] - the minimal space wasted after process nums[:x + 1] after y resizing operations
        dp = [[float("inf")] * (k + 1) for _ in range(L)]
        maxi = 0
        for x in range(L):
            maxi = max(maxi, nums[x])
            dp[x][0] = maxi * (x + 1) - presum[x + 1]
        # print(dp)

        # dp transfer
        # dp[x][y] = dp[]
        # dp[x][y] = min(dp[x][y], dp[k][y - 1] + waster space) for z in range(x - 1, 0)
        for x in range(L):
            for y in range(k):
                maxi = 0
                total = 0
                for z in range(x - 1, -1, -1):
                    maxi = max(maxi, nums[z + 1])
                    total += nums[z + 1]
                    wasted_space = maxi * (x - z) - total
                    dp[x][y + 1] = min(dp[x][y + 1], dp[z][y] + wasted_space)
        # print(dp)
        ans = min(dp[L - 1])
        return ans


nums = [10,20]
k = 0

nums = [10,20,30]
k = 1

nums = [10,20,15,30,20]
k = 2

nums = [1]
k = 0

nums = [10,20,15,30,20,15,20,15,30,30,45,15,20]
k = 3

solution = Solution()
print(solution.minSpaceWastedKResizing(nums, k))
