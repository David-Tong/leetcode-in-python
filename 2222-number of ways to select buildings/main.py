class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp init
        # zeros[y] - the number of ways ended with 0, with a length of y + 1, y can be 0, 1, 2
        # ones[y] - the number of ways ended with 1, with a length of y + 1, y can be 0, 1, 2
        N = 3
        zeros = [0] * N
        ones = [0] * N

        # dp transfer
        M = len(s)
        for x in range(M):
            if s[x] == "0":
                zeros[0] += 1
            elif s[x] == "1":
                ones[0] += 1
            if x > 0:
                if s[x] == "0":
                    zeros[1] += ones[0]
                    zeros[2] += ones[1]
                elif s[x] == "1":
                    ones[1] += zeros[0]
                    ones[2] += zeros[1]
        #print(zeros)
        #print(ones)
        ans = zeros[2] + ones[2]
        return ans


s = "001101"
s = "11100"

import random
s = "".join([random.choice(["0", "1"]) for _ in range(10 ** 3)])
print(s)

solution = Solution()
print(solution.numberOfWays(s))
