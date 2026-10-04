class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # pre-process
        L = len(stones)

        # prefix sums
        presums = [0]
        for stone in stones:
            presums.append(presums[-1] + stone)

        # process
        # A[x] = presums[x + 1]
        A = [presums[x + 1] for x in range(L)]

        # dp init
        # dp - the maximum score a player can get from the ith index of stones
        dp = [0] * L
        dp[L - 1] = 0

        # C[x] - A[x] - dp[x]
        C = [0] * L
        C[L - 1] = A[L - 1] - dp[L - 1]

        # suffix array
        # the maximum C[x] from x to L - 1
        suffix_max = [float("-inf")] * (L + 1)
        suffix_max[L - 1] = C[L - 1]

        # dp transfer
        for x in range(L - 2, -1, -1):
            dp[x] = suffix_max[x + 1]
            C[x] = A[x] - dp[x]
            suffix_max[x] = max(C[x], suffix_max[x + 1])

        ans = dp[0]
        return ans


stones = [-1,2,-3,4,-5]
stones = [7,-6,5,10,5,-2,-6]
stones = [-10,-12]

from random import randint
stones = [randint(-10 ** 4, 10 ** 4) for _ in range(10 ** 5)]
print(stones)

solution = Solution()
print(solution.stoneGameVIII(stones))