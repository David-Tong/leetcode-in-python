class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        M = len(nums1)
        N = len(nums2)

        # dp[x][y] - LCS for nums1[:x + 1] and nums2[:y + 1]
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for x in range(M):
            for y in range(N):
                if nums1[x] == nums2[y]:
                    dp[x + 1][y + 1] = max(dp[x + 1][y + 1], dp[x][y] + 1)
                else:
                    dp[x + 1][y + 1] = max(dp[x + 1][y + 1], max(dp[x][y + 1], dp[x + 1][y]))
        return dp[M][N]


nums1 = [1,4,2]
nums2 = [1,2,4]

nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]

nums1 = [1,3,7,1,7,5]
nums2 = [1,9,2,5,1]

nums1 = [1]
nums2 = [1]

nums1 = [1,2,3,4,5,6,7,8,9]
nums2 = [1,1,2,3,4,5,6,7,8,9]

solution = Solution()
print(solution.maxUncrossedLines(nums1, nums2))
