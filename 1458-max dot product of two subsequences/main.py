class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        M = len(nums1)
        N = len(nums2)

        # dp[x][y] - max dot product for subsequence in nums1[0 ... x] and nums2[0 ... y]
        dp = [[float("-inf")] * N for _ in range(M)]

        # transfer
        for x in range(M):
            for y in range(N):
                dp[x][y] = max(dp[x][y], nums1[x] * nums2[y])
                if y > 0:
                    dp[x][y] = max(dp[x][y], dp[x][y - 1])
                if x > 0:
                    dp[x][y] = max(dp[x][y], dp[x - 1][y])
                if x > 0 and y > 0:
                    dp[x][y] = max(dp[x][y], dp[x - 1][y - 1] + nums1[x] * nums2[y])

        # ans
        return dp[M - 1][N - 1]


nums1 = [2,1,-2,5]
nums2 = [3,0,-6]

nums1 = [3, -2]
nums2 = [2, -6, 7]

nums1 = [-1,-1]
nums2 = [1,1]

nums1 = [10,21,-8,-9,-15,-16]
nums2 = [-20,-9,11,23,1]

nums1 = [5]
nums2 = [-15]

nums1 = [-3,-8,3,-10,1,3,9]
nums2 = [9,2,3,7,-9,1,-8,5,-1,-1]

solution = Solution()
print(solution.maxDotProduct(nums1, nums2))
