class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        stack = []
        ans = ""
        for ch in command:
            if ch == "G":
                ans += ch
            elif ch == "(":
                stack.append(ch)
            elif ch == ")":
                piece = ""
                while len(stack) > 0 and stack[-1] != "(":
                    piece = stack[-1] + piece
                    stack.pop()
                if piece == "":
                    ans += "o"
                else:
                    ans += "al"
            else:
                stack.append(ch)
        return ans


command = "G()(al)"
command = "G()()()()(al)"
command = "(al)G(al)()()G"

solution = Solution()
print(solution.interpret(command))
