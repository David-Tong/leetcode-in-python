class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        idx = 0
        idx2 = 0

        ans = ""
        while idx < len(word1) and idx2 < len(word2):
            ans += word1[idx]
            ans += word2[idx2]
            idx += 1
            idx2 += 1

        while idx < len(word1):
            ans += word1[idx]
            idx += 1

        while idx2 < len(word2):
            ans += word2[idx2]
            idx2 += 1

        return ans


word1 = "abc"
word2 = "pqr"

word1 = "ab"
word2 = "pqrs"

word1 = "abcd"
word2 = "pq"

solution = Solution()
print(solution.mergeAlternately(word1, word2))
