import string


class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # process
        stack = list()
        for ch in s:
            if ch in string.digits:
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        ans = "".join(stack)
        return ans


s = "abc"
s = "cb34"

solution = Solution()
print(solution.clearDigits(s))
