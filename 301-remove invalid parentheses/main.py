class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.mini = len(s)
        self.anses = set()

        def doParentheses(s, stack, lefts, rights, removals):
            if len(s) == 0:
                if lefts == rights:
                    if removals < self.mini:
                        self.anses = set()
                        self.mini = removals
                    if removals <= self.mini:
                        self.anses.add("".join(stack))
            else:
                if s[0] == "(":
                    # put "(" in the stack
                    doParentheses(s[1:], stack[:] + [s[0]], lefts + 1, rights, removals)
                    # remove "("
                    if removals < self.mini:
                        doParentheses(s[1:], stack[:], lefts, rights, removals + 1)
                elif s[0] == ")":
                    # check if can put ")" in the stack
                    if lefts > rights:
                        doParentheses(s[1:], stack[:] + [s[0]], lefts, rights + 1, removals)
                    # remove ")"
                    if removals < self.mini:
                        doParentheses(s[1:], stack[:], lefts, rights, removals + 1)
                else:
                    # do nothing for a english letter
                    doParentheses(s[1:], stack[:] + [s[0]], lefts, rights, removals)

        # handle conner case
        ans = ""
        if not ")" in s:
            for ch in s:
                if ch == "(":
                    continue
                else:
                    ans += ch
            return [ans]
        elif not "(" in s:
            for ch in s:
                if ch == ")":
                    continue
                else:
                    ans += ch
            return [ans]

        doParentheses(s, [], 0, 0, 0)
        return list(self.anses)


s = "()())()"
s = "(a)())()"
#s = ")("
s = "((((((((((((((((((((aaaaa"

solution = Solution()
print(solution.removeInvalidParentheses(s))