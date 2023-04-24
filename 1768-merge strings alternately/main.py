class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        L = min(len(word1), len(word2))

        ans = ""
        for idx in range(L):
            ans += word1[idx] + word2[idx]

        if len(word1) > L:
            ans += word1[idx + 1:]
        if len(word2) > L:
            ans += word2[idx + 1:]

        return ans


word1 = "abc"
word2 = "pqr"

word1 = "ab"
word2 = "pqrs"

word1 = "abcd"
word2 = "pq"

solution = Solution()
print(solution.mergeAlternately(word1, word2))
