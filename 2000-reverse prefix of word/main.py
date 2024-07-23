class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ans = word
        for idx, c in enumerate(word):
            if c == ch:
                ans = word[:idx + 1][::-1] + word[idx + 1:]
                return ans
        return ans


word = "abcdefd"
ch = "d"

word = "xyxzxe"
ch = "z"

word = "abcd"
ch = "z"

solution = Solution()
print(solution.reversePrefix(word, ch))
