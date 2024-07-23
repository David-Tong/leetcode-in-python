class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        L = len(s)

        ones = list()
        for idx, ch in enumerate(s):
            if ch == "1":
                ones.append(idx)

        # process
        ans = 0
        if len(ones) == 0:
            ans = (L - 1) * (L - 2) // 2
        elif len(ones) % 3 == 0:
            S = len(ones) // 3
            ans = (ones[S] - ones[S - 1]) * (ones[2 * S] - ones[2 * S - 1])

        ans = ans % MODULO
        return ans


s = "10101"
s = "1001"
s = "0000"
s = "1101010101010101010101010011"

solution = Solution()
print(solution.numWays(s))
