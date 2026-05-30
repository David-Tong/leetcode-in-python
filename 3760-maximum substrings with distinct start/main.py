class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        # process
        st = set()
        ans = 0
        for ch in s:
            if ch not in st:
                ans += 1
                st.add(ch)
        return ans


s = "abab"
s = "abcd"
s = "aaaa"

import random
import string
s = "".join(random.choice(string.ascii_lowercase) for _ in range(10 ** 5))
print(s)

solution = Solution()
print(solution.maxDistinct(s))
