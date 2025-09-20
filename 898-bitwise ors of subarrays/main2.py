class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # general method to use dp to handle subarray problems
        # pre-process
        L = len(arr)

        # process
        # dp init
        # dp[x][y] - the result of bitwise or for arr[x: y+1]
        dp = [[0] * L for _ in range(L)]
        for x in range(L):
            dp[x][x] = arr[x]

        # dp transfer
        # dp[x][y] - dp[x][y-1] or arr[y]
        for x in range(L):
            for y in range(x + 1, L):
                dp[x][y] = dp[x][y - 1] | arr[y]
        # print(dp)

        # post-process
        s = set()
        for x in range(L):
            for y in range(x, L):
                s.add(dp[x][y])
        ans = len(s)
        return ans


arr = [0]
arr = [1,1,2]
arr = [1,2,4]
arr = [1,2,7,4]
arr = [1,2,4,7]

solution = Solution()
print(solution.subarrayBitwiseORs(arr))
