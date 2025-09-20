class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        # process
        ans = 0
        for pattern in patterns:
            if pattern in word:
                ans += 1
        return ans


patterns = ["a","abc","bc","d"]
word = "abc"

patterns = ["a","b","c"]
word = "aaaaabbbbb"

patterns = ["a","a","a"]
word = "ab"

solution = Solution()
print(solution.numOfStrings(patterns, word))
