class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        N = len(questions)

        # short-cut
        if N == 1:
            return questions[0][0]

        # dp[x][y] - the maximum points earned after solved xth question
        #            and unable to solve next y question
        from collections import defaultdict
        prev = defaultdict(int)
        prev[0] = 0
        prev[questions[0][1] + 1] = questions[0][0]

        for x in range(1, N):
            curr = defaultdict(int)
            for y in prev.keys():
                if y == 0:
                    curr[y] = max(curr[y], prev[y])
                else:
                    curr[y - 1] = max(curr[y - 1], prev[y])
            curr[questions[x][1] + 1] = max(curr[questions[x][1] + 1], curr[0] + questions[x][0])
            prev = curr

        return max(curr.values())


questions = [[3,2],[4,3],[4,4],[2,5]]
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
questions = [[1,1]]
questions = [[3,1],[5,6],[2,1],[2,3],[8,10],[5,2],[5,7],[2,1]]
questions = [[3,1],[5,6],[2,1],[2,3],[8,10],[5,2],[5,7],[2,1],[80,1]]
questions = [[43,5]]
questions = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]

solution = Solution()
print(solution.mostPoints(questions))