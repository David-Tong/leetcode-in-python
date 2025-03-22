class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        vowels = ['a', 'e', 'i', 'o', 'u']
        presums = [0]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                presums.append(presums[-1] + 1)
            else:
                presums.append(presums[-1])

        # process
        ans = list()
        for query in queries:
            start, end = query[0], query[1] + 1
            ans.append(presums[end] - presums[start])
        return ans


words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]

solution = Solution()
print(solution.vowelStrings(words, queries))
