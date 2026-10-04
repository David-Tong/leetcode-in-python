class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        L = len(word)

        # process
        ans = 0
        idx = 1
        while idx < L:
            if abs(ord(word[idx]) - ord(word[idx - 1])) <= 1:
                ans += 1
                idx += 1
            idx += 1
        return ans


word = "aaaaa"
word = "abddez"
word = "zyxyxyz"

solution = Solution()
print(solution.removeAlmostEqualCharacters(word))
