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
        # improvement one : use presum to reduce time complexity
        # improvement two : use rolling array to reduce space complexity
        # use dp to solve the ways to select 0 to k - T - 1 letters from counts letters
        # dp[x][y + 1] = the presum of the ways to
        #                   select y letters from 0 to x letters in counts letters
        C = k - T
        # init dp
        prev = [0] * (C + 1)
        for y in range(C):
            if y < counts[0]:
                prev[y + 1] = prev[y] + 1
            else:
                prev[y + 1] = prev[y]

        # dp transfer
        for x in range(1, T):
            dp = [0] * (C + 1)
            for y in range(C):
                lower = max(0, y + 1 - counts[x])
                dp[y + 1] = (prev[y + 1] - prev[lower] + dp[y]) % MODULO
            prev = dp
        # print(dp)
        ans = total - prev[C] % MODULO
        if ans < 0:
            ans += MODULO
        return ans


word = "aabbccdd"
k = 7

"""
word = "aabbccdd"
k = 8

word = "aaabbb"
k = 3

word = "dfkhuiefbweuffffffghhhhhshfweifhelfiiiiifsiwiwiwiwwweeeeifiifiigigpppppppwww"
k = 15

word = "abcd"
k = 4

word = "a"
k = 2
"""

word = "ooo"
k = 2

solution = Solution()
print(solution.possibleStringCount(word, k))