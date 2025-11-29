class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # process
        stack = list()
        for ch in s:
            if ch == 'c':
                if len(stack) > 1:
                    if stack[-1] == 'b' and stack[-2] == 'a':
                        stack.pop()
                        stack.pop()
                        continue
            stack.append(ch)

        ans = len(stack) == 0
        return ans


s = "aabcbc"
s = "abcabcababcc"
s = "abccba"
s = "abacbcabcc"

solution = Solution()
print(solution.isValid(s))
