class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def doBackspace(s):
            stack = []
            for ch in s:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return "".join(stack)

        s = doBackspace(s)
        t = doBackspace(t)

        return s == t


s = "ab#c"
t = "ad#c"

s = "ab##"
t = "c#d#"

s = "a#c##"
t = "b#"

solution = Solution()
print(solution.backspaceCompare(s, t))
