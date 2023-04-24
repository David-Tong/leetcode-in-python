class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        M = len(target)
        N = len(words[0])

        # pre-process
        dicts = dict()
        chs = set()
        for word in words:
            for ch in word:
                chs.add(ch)
        for ch in chs:
            dicts[ch] = [0] * N

        for idx, word in enumerate(words):
            for idx2, ch in enumerate(word):
                dicts[ch][idx2] += 1

        # short-cut
        for ch in target:
            if ch not in dicts:
                return 0

        # dp[x][y] - number of ways after xth character of target is selected
        #            and with yth character of any string in words used
        dp = [[0] * N for _ in range(M)]
        presum = [[] * N for _ in range(M)]

        for x in range(M):
            if x == 0:
                for y in range(x, N):
                    ch = target[x]
                    dp[x][y] = dicts[ch][y]
            else:
                ch = target[x]
                for idx, count in enumerate(dicts[ch]):
                    if idx >= x:
                        dp[x][idx] += count * presum[x - 1][idx - 1]

            # calculate presum
            total = 0
            for y in range(N):
                total += dp[x][y]
                presum[x].append(total)

        return sum(dp[M - 1]) % MODULO


words = ["acca","bbbb","caca"]
target = "aba"

words = ["abba","baab"]
target = "bab"

words = ["asrefbjkdh"]
target = "dh"

words = ["abcdefghijkl", "bcdefghijlzk", "aeiuwefdftyx"]
target = "acf"

words = ["ddcc","bdcb","bdbb"]
target = "bab"

solution = Solution()
print(solution.numWays(words, target))
