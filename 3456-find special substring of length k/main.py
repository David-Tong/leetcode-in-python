class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # pre-process
        L = len(s)

        # helper function
        # validate
        def validate(x):
            if x > 0:
                if s[x] == s[x - 1]:
                    return False
            if x + k < L:
                if s[x + k - 1] == s[x + k]:
                    return False
            for y in range(k):
                if s[x + y] != s[x]:
                    return False
            return True

        # process
        for x in range(L):
            if x + k <= L:
                if validate(x):
                    return True
        return False


s = "aaabaaa"
k = 3

s = "abc"
k = 2

s = "aaaabaaaa"
k = 3

s = "h"
k = 1

s = "jkjhfgg"
k = 2

solution = Solution()
print(solution.hasSpecialSubstring(s, k))
