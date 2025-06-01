class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        # process
        ans = list()
        for idx, word in enumerate(words):
            for ch in word:
                if ch == x:
                    ans.append(idx)
                    break
        return ans


words = ["leet","code"]
x = "e"

words = ["abc","bcd","aaaa","cbc"]
x = "a"

words = ["abc","bcd","aaaa","cbc"]
x = "z"

solution = Solution()
print(solution.findWordsContaining(words, x))
