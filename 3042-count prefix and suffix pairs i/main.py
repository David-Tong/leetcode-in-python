class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        L = len(words)
        ans = 0
        for x in range(L):
            for y in range(x + 1, L):
                word = words[x]
                l = len(word)
                if word == words[y][:l] and word == words[y][-l:]:
                    ans += 1
        return ans


words = ["a","aba","ababa","aa"]
words = ["pa","papa","ma","mama"]
words = ["abab","ab"]
words = ["a","a","a"]

solution = Solution()
print(solution.countPrefixSuffixPairs(words))
