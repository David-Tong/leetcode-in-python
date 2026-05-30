class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        # pre-process
        words = text.split()
        L = len(words)

        spaces = 0
        for ch in text:
            if ch == " ":
                spaces += 1

        # process
        ans = ""
        if L > 1:
            space = spaces // (L - 1)
            remain = spaces % (L - 1)

            for word in words[:-1]:
                ans += word + " " * space
            ans += words[-1] + " " * remain
        else:
            ans += words[0] + " " * spaces
        return ans


text = "  this   is  a sentence "
text = " practice   makes   perfect"
text = "  a"

solution = Solution()
print(solution.reorderSpaces(text))
