class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        L = len(s)

        # process
        ans = ""

        idx = 0
        while idx < L:
            if s[idx] == "*":
                if len(ans) > 0:
                    ans = ans[:-1]
            elif s[idx] == "#":
                ans *= 2
            elif s[idx] == "%":
                ans = ans[::-1]
            else:
                ans += s[idx]
            idx += 1

        return ans


s = "a#b%*"
s = "z*#"

from string import ascii_lowercase
from random import choice
s = "".join(choice(ascii_lowercase + "*#%") for _ in range(20))
print(s)

solution = Solution()
print(solution.processStr(s))
