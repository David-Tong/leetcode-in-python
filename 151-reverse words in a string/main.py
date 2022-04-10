class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slow = 0
        fast = 0
        word = False
        stack = []
        while fast < len(s):
            if s[fast] == " ":
                if word:
                    stack.append((slow, fast - 1))
                    word = False
            else:
                if not word:
                    slow = fast
                    word = True
            fast += 1
        if word:
            stack.append((slow, fast - 1))

        ans = ""
        while len(stack) > 0:
            interval = stack.pop()
            ans += s[interval[0]:interval[1] + 1]
            ans += " "
        return ans[:-1]


s = "the sky is blue"
#s = "  hello world  "
#s = "a good   example"
s = "   good morning"
s = "nice afternoon "

solution = Solution()
print(solution.reverseWords(s))
