class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # init
        L = len(arr)
        dp = [0] * (L + 1)

        # transfer
        for x in range(L):
            maxi = float("-inf")
            for y in range(min(x + 1, k)):
                maxi = max(maxi, arr[x - y])
                dp[x + 1] = max(dp[x + 1], dp[x - y] + maxi * (y + 1))
        return dp[L]


arr = [1,15,7,9,2,5,10]
k = 3

arr = [2,1,4,3]
k = 3

arr = [1,4,1,5,7,3,6,1,9,9,3]
k = 4

arr = [1]
k = 1

solution = Solution()
print(solution.maxSumAfterPartitioning(arr, k))
