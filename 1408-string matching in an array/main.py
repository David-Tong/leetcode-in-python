class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        L = len(words)
        ans = set()
        for x in range(L):
            for y in range(L):
                if x != y and len(words[x]) < len(words[y]):
                    if words[x] in words[y]:
                        ans.add(words[x])
        ans = list(ans)
        return ans


words = ["mass","as","hero","superhero"]
words = ["leetcode","et","code"]
words = ["blue","green","bu"]
words = ["leetcoder","leetcode","od","hamlet","am"]

solution = Solution()
print(solution.stringMatching(words))
