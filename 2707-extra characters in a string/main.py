class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        L = len(s)

        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)

        for word in dictionary:
            dicts[len(word)].append(word)

        # dp[x] - the minimum number of extra characters left to break up s[:x] optimally
        dp = [float("inf")] * (L + 1)
        dp[0] = 0

        # dp
        for x in range(L):
            for y in range(x + 1):
                dp[x + 1] = min(dp[x + 1], x + 1 - y + dp[y])

            for y in dicts.keys():
                if x + 1 - y >= 0:
                    target = s[x + 1 - y: x + 1]
                    if target in dicts[y]:
                        dp[x + 1] = min(dp[x + 1], dp[x + 1 - y])

        return dp[L]


s = "leetscode"
dictionary = ["leet","code","leetcode"]

s = "sayhelloworld"
dictionary = ["hello","world"]

s = "a"
dictionary = ["a"]

s = "fooxxxbarxbarxbarbar"
dictionary = ["foo", "bar", "x"]

solution = Solution()
print(solution.minExtraChar(s, dictionary))
