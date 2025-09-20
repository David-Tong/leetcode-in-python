class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        # process
        ans = 0
        for word in text.split():
            can = True
            for ch in word:
                if ch in brokenLetters:
                    can = False
                    break
            if can:
                ans += 1
        return ans


text = "hello world"
brokenLetters = "ad"

text = "leet code"
brokenLetters = "lt"

text = "leet code"
brokenLetters = "e"

solution = Solution()
print(solution.canBeTypedWords(text, brokenLetters))
