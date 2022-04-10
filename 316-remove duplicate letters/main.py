class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = [0] * 26
        in_stack = [False] * 26
        stack = []

        for idx, ch in enumerate(s):
            pivot = ord(ch) - ord('a')
            last_index[pivot] = idx

        for idx, ch in enumerate(s):
            pivot = ord(ch) - ord('a')
            if in_stack[pivot]:
                continue

            while len(stack) > 0 and ord(stack[-1]) > ord(ch) and \
                last_index[ord(stack[-1]) - ord('a')] > idx:
                in_stack[ord(stack[-1]) - ord('a')] = False
                stack.pop()
            stack.append(ch)
            in_stack[pivot] = True
        return "".join(stack)


s = "bcabc"
s = "cbacdcbc"

solution = Solution()
print(solution.removeDuplicateLetters(s))
