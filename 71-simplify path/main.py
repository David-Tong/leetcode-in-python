class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tokens = []
        left = 0
        right = 1
        tokens.append(path[left])
        while right < len(path):
            if path[right] != "/":
                right += 1
            else:
                if left + 1 != right:
                    tokens.append(path[left + 1:right])
                left = right
                tokens.append(path[left])
                right += 1
        if left + 1 != right:
            tokens.append(path[left + 1:right])

        stack = []
        for token in tokens:
            if token == "/":
                if len(stack) == 0 or stack[-1] != "/":
                    stack.append(token)
            elif token == "..":
                if len(stack) > 1:
                    stack.pop()
                    stack.pop()
            elif token == ".":
                pass
            else:
                stack.append(token)

        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()

        ans = ""
        for token in stack:
            ans += token
        return ans


s = "/home/"
s = "/../"
s = "/home//foo/"
s = "/home/foo/../..//./bar"
s = "/..home/foo/.."

solution = Solution()
print(solution.simplifyPath(s))
