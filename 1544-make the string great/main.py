class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        from string import lower
        L = len(s)
        idx = 0
        stack = list()
        while idx < L:
            if stack and abs(ord(stack[-1]) - ord((s[idx]))) == 32:
                stack.pop()
            else:
                stack.append(s[idx])
            idx += 1

        return "".join(stack)


s = "leEeetcode"
s = "abBAcC"
s = "s"
s = "aaA"

solution = Solution()
print(solution.makeGood(s))
