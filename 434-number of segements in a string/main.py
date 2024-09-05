class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += ' '
        L = len(s)

        start = 0
        space = False
        word = False
        idx = 0
        ans = 0
        while idx < L:
            if s[idx] == " ":
                if not space:
                    if word:
                        ans += 1
                space = True
            else:
                if space:
                    start = idx
                word = True
                space = False
            idx += 1
        return ans


s = "Hello, my name is John"
s = "Hello"
s = "    Yes, sir"
s = "   I am cat   "
s = "hello   !"

solution = Solution()
print(solution.countSegments(s))
