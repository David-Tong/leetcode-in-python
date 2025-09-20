class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # dp init
        # dp[x][y] - the maximum length of valid subsequence in nums[:x + 1]
        #          - with the (sub[x - 1] + sub[x]) % k == y
        L = len(nums)
        dp = [[1] * k for _ in range(L)]

        # dp transfer
        # dp[x][y] = dp[d][y] + 1
        # d - (mod[x] + mod[d]) % k == y
        last = [-1] * k
        ans = 0
        for x in range(L):
            mod = nums[x] % k
            for y in range(k):
                d = (y - mod + k) % k
                if last[d] != -1:
                    dp[x][y] = dp[last[d]][y] + 1
                    ans = max(ans, dp[x][y])
            last[mod] = x
        # print(dp)
        # print(last)
        return ans


nums = [1,2,3,4,5]
k = 2

nums = [1,4,2,3,1,4]
k = 3

solution = Solution()
print(solution.maximumLength(nums, k))
