class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        # process
        # count - the number of ( to match
        idx, count = 0, 0
        ans = 0
        while idx < L:
            if s[idx] == "(":
                count += 1
            elif s[idx] == ")":
                if idx < L - 1 and s[idx + 1] == ")":
                    count -= 1
                    idx += 1
                else:
                    ans += 1
                    count -= 1

            if count < 0:
                ans += 1
                count += 1
            idx += 1

        # post-process
        ans += count * 2
        return ans


s = "(()))"
s = "())"
s = "))())("
"""
s = "))))()()()((()))((()"
s = "("
s = ")))))))"
s = "()())))()"
"""

solution = Solution()
print(solution.minInsertions(s))
