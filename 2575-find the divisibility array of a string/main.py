class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        # pre-process
        L = len(word)

        # process
        ans = list()
        total = 0
        idx = 0
        while idx < L:
            total = total * 10 + int(word[idx])
            if total % m == 0:
                ans.append(1)
            else:
                ans.append(0)
            total %= m
            idx += 1
        return ans


word = "998244353"
m = 3

word = "1010"
m = 10

import string
import random
word = "".join([random.choice(string.digits) for _ in range(10 ** 5)])
m = 10 ** 6
print(word)

solution = Solution()
print(solution.divisibilityArray(word, m))
