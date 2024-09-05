class Solution(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        """
        :type n: int
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        seq = [0]

        L = len(groups)
        for x in range(1, L):
            if groups[x] != groups[x - 1]:
                seq.append(x)

        ans = list()
        for idx in seq:
            ans.append(words[idx])
        return ans


n = 3
words = ["e","a","b"]
groups = [0,0,1]

"""
n = 4
words = ["a","b","c","d"]
groups = [1,0,1,1]
"""

n = 1
words = ["a"]
groups = [1]

solution = Solution()
print(solution.getWordsInLongestSubsequence(n, words, groups))
