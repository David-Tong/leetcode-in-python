class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # pre-process
        from math import sqrt
        N = int(sqrt(n))
        squares = set()
        for x in range(N):
            squares.add((x + 1) ** 2)

        # helper function
        # k - winner square game for k
        # who - 0 for alice, 1 for bob
        # return True for alice win else False
        def win(k, who):
            key = "{}-{}".format(k, who)
            if key in self.cache:
                return self.cache[key]

            if k in squares:
                res = who == 0
            else:
                K = int(sqrt(k))
                if who == 0:
                    res = False
                else:
                    res = True
                for x in range(K):
                    nxt = k - (x + 1) ** 2
                    if who == 0 and win(nxt, 1 - who):
                        res = True
                        break
                    if who == 1 and not win(nxt, 1 - who):
                        res = False
                        break
            self.cache[key] = res
            return res

        from collections import defaultdict
        self.cache = defaultdict(bool)

        return win(n, 0)


"""
expected results
[True, False, True, True, False, True, False, True, True, False, True]
"""
solution = Solution()
# print(solution.winnerSquareGame(7))

for n in range(1, 12):
    print(solution.winnerSquareGame(n))

"""
n = 10 ** 5

solution = Solution()
print(solution.winnerSquareGame(n))
"""