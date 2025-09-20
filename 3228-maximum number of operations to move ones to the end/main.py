class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        # process
        L = len(s)
        ones = 0
        ans = 0
        for x in range(L - 1):
            if s[x] == "1":
                ones += 1
                if s[x + 1] == "0":
                    ans += ones
        return ans


s = "1001101"
s = "00111"

from random import randint
s = "".join([str(randint(0, 1)) for _ in range(100)])
print(s)

from random import randint
s = "".join([str(randint(0, 1)) for _ in range(10 ** 3)])
print(s)


solution = Solution()
print(solution.maxOperations(s))
