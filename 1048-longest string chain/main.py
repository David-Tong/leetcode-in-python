class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(set)
        dp = defaultdict(int)

        for word in words:
            dicts[len(word)].add(word)
            dp[word] = 1

        for key in sorted(dicts.keys()):
            if key == 1:
                continue
            else:
                for word in dicts[key]:
                    for x in range(key):
                        predecessor = word[:x] + word[x+1:]
                        if predecessor in dicts[key - 1]:
                            dp[word] = max(dp[word], dp[predecessor] + 1)

        return max(dp.values())


words = ["a","b","ba","bca","bda","bdca"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
words = ["abcd","dbqca"]

solution = Solution()
print(solution.longestStrChain(words))
