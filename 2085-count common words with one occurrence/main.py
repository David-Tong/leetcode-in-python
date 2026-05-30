class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts1 = defaultdict(int)
        dicts2 = defaultdict(int)

        for word1 in words1:
            dicts1[word1] += 1

        for word2 in words2:
            dicts2[word2]+= 1

        # process
        ans = 0
        for word in dicts1:
            if dicts1[word] == dicts2[word] == 1:
                ans += 1
        return ans


words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

solution = Solution()
print(solution.countWords(words1,words2))