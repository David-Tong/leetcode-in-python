class Solution(object):
    def removeSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # pre-process
        L = len(s)

        # process
        stack = list()
        stack2 = list()
        idx = 0
        left, right = 0, 0
        while idx < L:
            ch = s[idx]
            stack.append(ch)
            if ch == "(":
                if right > 0:
                    stack2.append((left, right))
                    left, right = 0, 0
                left += 1
            elif ch == ")":
                right += 1
                if left >= right >= k:
                    idx2 = 0
                    while idx2 < k * 2:
                        stack.pop()
                        idx2 += 1
                    if stack:
                        if stack[-1] == ")":
                            left, right = stack2.pop()
                        elif stack[-1] == "(":
                            right -= k
                            left -= k
            idx += 1
        ans = "".join(stack)
        return ans


s = "(())"
k = 1

s = "(()("
k = 1

s = "((()))()()()"
k = 3

s = "(((((())))))"
k = 3

s = "(((((()))))()"
k = 3

s = "(()(()(()))((()"
k = 2

"""
from random import choice
s = "".join(choice("()") for _ in range(30))
k = 2
print(s)
"""

solution = Solution()
print(solution.removeSubstring(s, k))
