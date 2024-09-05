class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        N = len(questions)

        # dp[x]    - the maximum points earned before solving xth question
        # maxi[x]     - the maximum points earned after solving xth question
        dp = [0] * N
        maxi = [0] * N
        successor = questions[0][1] + 1
        if successor < N:
            dp[successor] = questions[0][0]
        maxi[0] = questions[0][0]

        from heapq import heapify, heappush
        heap = list()
        heapify(heap)

        for x in range(1, N):
            heappush(heap, dp[x] * -1)
            top = heap[0] * -1
            successor = x + questions[x][1] + 1
            if successor < N:
                dp[successor] = max(dp[successor], top + questions[x][0])
            maxi[x] = max(maxi[x], top + questions[x][0])

        return max(maxi)


questions = [[3,2],[4,3],[4,4],[2,5]]
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
questions = [[1,1]]
questions = [[3,1],[5,6],[2,1],[2,3],[8,10],[5,2],[5,7],[2,1]]
questions = [[3,1],[5,6],[2,1],[2,3],[8,10],[5,2],[5,7],[2,1],[80,1]]
questions = [[43,5]]
questions = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]

solution = Solution()
print(solution.mostPoints(questions))
