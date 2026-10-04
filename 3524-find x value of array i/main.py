class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        # process
        # dp[x][y] - the number of subarray of nums[:x+1] with the product mod k as y

        # dp init
        dp = [[0] * k for _ in range(L)]
        m = nums[0] % k
        dp[0][m] = 1

        # dp transfer
        for x in range(1, L):
            m = nums[x] % k
            dp[x][m] = 1
            for y in range(k):
                m = y * nums[x] % k
                dp[x][m] += dp[x - 1][y]

        # post process
        ans = [0] * k
        for x in range(L):
            for y in range(k):
                ans[y] += dp[x][y]
        return ans


nums = [1,2,3,4,5]
k = 3

nums = [1,2,4,8,16,32]
k = 4

nums = [1,1,2,1,1]
k = 2

solution = Solution()
print(solution.resultArray(nums, k))
