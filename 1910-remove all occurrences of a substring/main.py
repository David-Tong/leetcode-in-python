class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        # pre-process
        L = len(part)

        # process
        stack = list()
        for ch in s:
            stack.append(ch)
            if len(stack) >= L:
                if "".join(stack[-L:]) == part:
                    # pop all
                    for x in range(L):
                        stack.pop()

        # post-process
        ans = "".join(stack)
        return ans


s = "daabcbaabcbc"
part = "abc"

s = "axxxxyyyyb"
part = "xy"

s = "x"
part = "x"

solution = Solution()
print(solution.removeOccurrences(s, part))
