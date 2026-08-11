class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        L = len(word)

        # process
        ans = 0
        idx = 0
        pushes = 1
        while idx <= L:
            ans += min(L - idx, 8) * pushes
            pushes += 1
            idx += 8
        return ans


word = "abcde"
word = "xycdefghij"
word = "abcdefghijklmnopqrstuvwxyz"

solution = Solution()
print(solution.minimumPushes(word))
