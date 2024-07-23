class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list()
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                temp = list()
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(ch)
        ans = "".join(stack)
        return ans


s = "(abcd)"
s = "(u(love)i)"
s = "(ed(et(oc))el)"
s = "(ed(et(oc))eel)"
s = "ta()usw((((a))))"

solution = Solution()
print(solution.reverseParentheses(s))
