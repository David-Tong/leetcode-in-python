class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        N = 26
        bits = [0] * 26
        for x in range(N):
            bits[x] = 2 ** x

        def encode(word):
            code = 0
            for ch in word:
                bit = ord(ch) - ord('a')
                code |= bits[bit]
            return code

        codes = [(encode(word), len(word))for word in words]
        L = len(codes)
        ans = 0
        for x in range(L):
            for y in range(x+1, L):
                if codes[x][0] & codes[y][0] == 0:
                    ans = max(ans, codes[x][1] * codes[y][1])
        return ans


words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words = ["a","ab","abc","d","cd","bcd","abcd"]
words = ["a","aa","aaa","aaaa"]

solution = Solution()
print(solution.maxProduct(words))
