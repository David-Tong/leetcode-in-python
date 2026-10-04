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

        # dp init
        # base case
        dp = [0] * L
        dp[L - 1] = 0

        # dp transfer
        for x in range(L - 2, -1, -1):
            min_max = float("-inf")
            # y is the next index to start for opponent
            for y in range(x + 1, L):
                score = presums[y + 1]
                best = max(min_max, score - dp[y])
            dp[x] = min_max

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