class Solution(object):
    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        # helper function
        def adjacent(ch, ch2):
            if ch == 'a' and ch2 == 'z' or \
                ch == 'z' and ch2 == 'a':
                return True
            elif abs(ord(ch) - ord(ch2)) == 1:
                return True
            else:
                return False

        # process
        stack = list()
        for ch in s:
            if stack and adjacent(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        ans = "".join(stack)
        return ans


s = "abc"
s = "adcb"
s = "zadb"

solution = Solution()
print(solution.resultingString(s))
