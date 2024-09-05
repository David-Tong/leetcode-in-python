class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()
        ans = 0
        depth = 0
        for ch in s:
            if ch == "(":
                depth += 1
                ans = max(ans, depth)
            elif ch == ")":
                depth -= 1
        return ans


s = "(1+(2*3)+((8)/4))+1"
s = "(1)+((2))+(((3)))"
s = "1+2+3"


solution = Solution()
print(solution.maxDepth(s))
