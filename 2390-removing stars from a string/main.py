class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list()
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


s = "leet**cod*e"
s = "erase*****"
s = "dff******"

solution = Solution()
print(solution.removeStars(s))
