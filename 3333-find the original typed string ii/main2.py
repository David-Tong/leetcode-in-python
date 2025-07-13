class Solution(object):
    def possibleStringCount(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # conner case
        L = len(word)
        if L < k:
            return 0
        elif L == k:
            return 1

        # pre-process
        # counts to record the letter group, for a letter being typed one or multiple times
        MODULO = 10 ** 9 + 7
        count, counts = 1, list()
        idx = 1
        while idx < L:
            if word[idx - 1] == word[idx]:
                count += 1
            else:
                counts.append(count)
                count = 1
            idx += 1
        counts.append(count)
        # print(counts)

        T = len(counts)
        total = 1
        for x in range(T):
            total = (total * counts[x]) % MODULO
        # conner case
        if T >= k:
            return total
        # print(total)

        # process
        # use dp to solve the ways to select 0 to k - T - 1 letters from counts letters
        # dp[x][y] = the ways to select y letters from 0 to x letters in counts letters
        C = k - T
        dp = [[0] * C for _ in range(T)]
        for x in range(T):
            for y in range(C):
                if x == 0:
                    if y < counts[x]:
                        dp[x][y] = 1
                else:
                    for z in range(y, max(-1, y - counts[x]), -1):
                        dp[x][y] = (dp[x][y] + dp[x - 1][z]) % MODULO
        print(dp)
        ans = total - sum(dp[T - 1]) % MODULO
        if ans < 0:
            ans += MODULO
        return ans


word = "aabbccdd"
k = 7


word = "aabbccdd"
k = 8

word = "aaabbb"
k = 3

word = "dfkhuiefbweuffffffghhhhhshfweifhelfiiiiifsiwiwiwiwwweeeeifiifiigigpppppppwww"
k = 15

"""
word = "abcd"
k = 4

word = "a"
k = 2
"""

solution = Solution()
print(solution.possibleStringCount(word, k))
