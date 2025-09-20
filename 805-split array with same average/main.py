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
        M = sum(nums)

        # dp init
        # dp[x][y] - we have x elements in nums for a sum of y
        from collections import defaultdict
        dp = [set() for _ in range(N + 1)]
        dp[0].add(0)

        # dp transfer
        # dp[x][y] - dp[x - num][y - 1] if True
        for num in nums:
            for x in range(N - 1, -1, -1):
                for y in dp[x]:
                    curr = y + num
                    dp[x + 1].add(curr)
                    if x + 1 < N:
                        if curr * N == M * (x + 1):
                            return True
            # print(dp)
        return False


nums = [1,2,3,4,5,6,7,8]
nums = [3,1]
nums = [2509, 8789, 4362, 1142, 3509, 4016, 5771, 9001, 7348, 810, 6361, 6104, 2806, 2846, 2849]
nums = [9507, 9480, 4838, 7549, 6165, 3618, 718, 4792, 2683, 3525, 3759, 6509, 1262, 1674, 8490, 3656, 5125, 354, 5778, 9219]
nums = [8896, 8367, 8093, 2072, 5074, 8254, 8662, 9761, 4551, 9961, 8685, 9605, 4341, 9116, 2159, 4146, 2564, 8062, 1053, 173, 2696, 4589, 3166, 7863, 1884]
nums = [3915, 2495, 3563, 6954, 4106, 7787, 1599, 9000, 6362, 8191, 6928, 3768, 105, 9323, 8612, 4, 1815, 429, 3214, 7102, 6528, 4829, 6230, 1651, 7833, 3073, 463, 6175, 1123, 6885]
nums = [3,1,2]
# nums = [2,12,18,16,19,3]
# nums = [41,8467,6334,6500,9169,5724,1478,9358,6962,4464,5705,8145,3281,6827,9961,491,2995,1942,4827,5436,2391,4604,3902,153,292,2382,7421,8716,9718,9895]

solution = Solution()
print(solution.splitArraySameAverage(nums))