class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # pre-process
        L = len(score)
        idx = [_ for _ in range(L)]
        scores = zip(score, idx)
        scores = sorted(scores, reverse=True)

        # process
        ans = [""] * L
        for idx, scr in enumerate(scores):
            _, rank = scr
            if idx == 0:
                ans[rank] = "Gold Medal"
            elif idx == 1:
                ans[rank] = "Silver Medal"
            elif idx == 2:
                ans[rank] = "Bronze Medal"
            else:
                ans[rank] = str(idx + 1)
        return ans


score = [5,4,3,2,1]
score = [10,3,8,9,4]

solution = Solution()
print(solution.findRelativeRanks(score))
