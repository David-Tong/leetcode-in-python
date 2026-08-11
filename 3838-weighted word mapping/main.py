class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        # pre-process
        MOD = 26

        # helper function
        def decode(word, weights):
            res = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                res += weights[idx]
            res %= MOD
            return res

        def map(num):
            return chr(ord('z') - num)

        # process
        ans = ""
        for word in words:
            ans += map(decode(word, weights))
        return ans


words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

words = ["a","b","c"]
weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

words = ["abcd"]
weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]

solution = Solution()
print(solution.mapWordWeights(words, weights))
