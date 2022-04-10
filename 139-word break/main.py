class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        N = len(s) + 1
        dp = [False] * N
        dp[0] = True
        for x in range(N):
            for y in range(20):
                if x + y + 1 < N and s[x: x + y + 1] in wordDict:
                    if not dp[x + y + 1]:
                        dp[x + y + 1] = True & dp[x]
        return dp[N - 1]


s = "leetcode"
wordDict = ["leet", "code"]

s = "applepenapple"
wordDict = ["apple", "pen"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "a"
wordDict = ["a"]

s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]

solution = Solution()
print(solution.wordBreak(s, wordDict))
