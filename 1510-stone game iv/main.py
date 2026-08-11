class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # pre-process
        from math import sqrt
        N = int(sqrt(n))
        squares = set((x + 1) ** 2 for x in range(N))

        # process
        # dp init
        # dp[k][who] = True if who removes square number stones from k stones and Alice wins
        # who: 0 = Alice, 1 = Bob
        dp = [[False, False] for _ in range(n + 1)]

        # dp transfer
        for k in range(1, n + 1):
            K = int(sqrt(k))

            for who in (0, 1):
                # case 1: k is a perfect square
                if k in squares:
                    dp[k][who] = (who == 0)
                    continue

                # case 2: try all moves
                win_flag = who == 1
                for x in range(K):
                    nxt = k - (x + 1) ** 2
                    if nxt > 0:
                        # if opponent loses, current player wins
                        if who == 0 and dp[nxt][1 - who]:
                            win_flag = True
                            break
                        if who == 1 and not dp[nxt][1 - who]:
                            win_flag = False
                            break
                dp[k][who] = win_flag
        # print(dp)
        return dp[n][0]



"""
expected results
[True, False, True, True, False, True, False, True, True, False, True]
"""

n = 1
n = 2
n = 3
n = 4
n = 11
# n = 10 ** 3
# n = 10 ** 4
# n = 10 ** 5

solution = Solution()
print(solution.winnerSquareGame(n))