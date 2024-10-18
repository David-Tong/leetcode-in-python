class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += " "
        stack = list()
        for c in s:
            while len(stack) > 1 and \
                    ((stack[-2] == "A" and stack[-1] == "B") or \
                    (stack[-2] == "C" and stack[-1] == "D")):
                stack.pop()
                stack.pop()
            stack.append(c)

        stack.pop()
        ans = len(stack)
        return ans


s = "ABFCACDB"
s = "ACBBD"
s = "ABFACDBAB"

solution = Solution()
print(solution.minLength(s))
