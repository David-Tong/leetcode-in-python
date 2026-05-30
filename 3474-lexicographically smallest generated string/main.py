class Solution(object):
    def generateString(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # pre-process
        N = len(str1)
        M = len(str2)

        # process
        ans = [' '] * (N + M - 1)
        mandatory = [False] * (N + M - 1)

        # step 1 : place all "T" positions
        idx = 0
        while idx < N:
            if str1[idx] == 'T':
                idx2 = 0
                while idx2 < M:
                    if ans[idx + idx2] == ' ':
                        ans[idx + idx2] = str2[idx2]
                        mandatory[idx + idx2] = True
                    else:
                        if ans[idx + idx2] != str2[idx2]:
                            return ""
                    idx2 += 1
            idx += 1

        # step 2 : place all "F"
        idx = 0
        while idx < N + M - 1:
            if ans[idx] == ' ':
                ans[idx] = 'a'
            idx += 1

        # step 3 : validate all "F" positions
        idx = 0
        while idx < N:
            if str1[idx] == 'F':
                temp = "".join(ans[idx:idx + M])
                if temp == str2:
                    idx2 = idx + M - 1
                    while idx2 >= idx:
                        if not mandatory[idx2]:
                            break
                        idx2 -= 1
                    if idx2 < idx:
                        return ""
                    ans[idx2] = 'b'
            idx += 1

        return "".join(ans)


str1 = "TFTF"
str2 = "ab"

"""
str1 = "TFTF"
str2 = "abc"

str1 = "F"
str2 = "d"

import random
import string
str1 = "".join([random.choice("TFFFFFFFFF") for _ in range(10 ** 3)])
str2 = "".join([random.choice(string.ascii_lowercase) for _ in range(10)])
print(str1)
print(str2)

str1 = "F"
str2 = "acfcfc"

str1 = "TTFFT"
str2 = "fff"

str1 = "FFTFFF"
str2 = "a"
"""

solution = Solution()
print(solution.generateString(str1, str2))
