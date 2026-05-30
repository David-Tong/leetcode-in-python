class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        tokens = s.split()
        L = len(tokens)

        # process
        words = [''] * L
        for word in s.split():
            idx = int(word[-1:])
            words[idx - 1] = word[:-1]

        ans = " ".join(words)
        return ans


s = "is2 sentence4 This1 a3"
s = "Myself2 Me1 I4 and3"

solution = Solution()
print(solution.sortSentence(s))
