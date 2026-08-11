class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        ones = 0
        zeros = list()
        zero = 0
        idx = 0
        while idx < L:
            if s[idx] == "1":
                ones += 1
                if zero > 0:
                    zeros.append(zero)
                    zero = 0
            else:
                zero += 1
            idx += 1
        if zero > 0:
            zeros.append(zero)
        # print(zeros)

        # process
        N = len(zeros)
        ans = 0
        idx = 1
        while idx < N:
            ans = max(ans, zeros[idx] + zeros[idx - 1])
            idx += 1
        ans += ones
        return ans


s = "01"
s = "0100"
s = "1000100"
s = "01010"
s = "0101100011100"

from random import choice
s = "".join(choice("01") for _ in range(10 ** 5))
print(s)

solution = Solution()
print(solution.maxActiveSectionsAfterTrade(s))
