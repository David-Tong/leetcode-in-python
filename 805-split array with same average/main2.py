class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # since the subarray average must be equal to nums average
        # so once we find a subarray with the target average, and it doesn't include the whole array
        # we may return True

        # pre-process
        N = len(nums)
        M = 10 ** 4 * N
        E = 1e-5
        target = sum(nums) * 1.0 / N

        # dp init
        # dp[x][y] - if we have the sum x with a subarray of length y
        from collections import defaultdict
        dp = [[False] * (N + 1) for _ in range(M)]
        dp[0][0] = True

        # dp transfer
        # dp[x][y] - dp[x - num][y - 1] if True
        for num in nums:
            for x in range(M):
                for y in range(N):
                    if dp[x - num][y]:
                        dp[x][y + 1] = True
                        average = x * 1.0 / (y + 1)
                        if abs(average - target) <= E:
                            if y + 1 < N:
                                return True
        return False


nums = [1,2,3,4,5,6,7,8]
nums = [3,1]
nums = [2509, 8789, 4362, 1142, 3509, 4016, 5771, 9001, 7348, 810, 6361, 6104, 2806, 2846, 2849]
nums = [9507, 9480, 4838, 7549, 6165, 3618, 718, 4792, 2683, 3525, 3759, 6509, 1262, 1674, 8490, 3656, 5125, 354, 5778, 9219]
nums = [8896, 8367, 8093, 2072, 5074, 8254, 8662, 9761, 4551, 9961, 8685, 9605, 4341, 9116, 2159, 4146, 2564, 8062, 1053, 173, 2696, 4589, 3166, 7863, 1884]
nums = [3915, 2495, 3563, 6954, 4106, 7787, 1599, 9000, 6362, 8191, 6928, 3768, 105, 9323, 8612, 4, 1815, 429, 3214, 7102, 6528, 4829, 6230, 1651, 7833, 3073, 463, 6175, 1123, 6885]
# nums = [3,1,2]


solution = Solution()
print(solution.splitArraySameAverage(nums))
