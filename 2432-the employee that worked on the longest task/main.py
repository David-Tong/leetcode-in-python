class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        ans = (float("inf"), 0)
        prev = 0
        for id, leave in logs:
            time = leave - prev
            prev = leave
            if time > ans[1]:
                ans = (id, time)
            elif time == ans[1]:
                if ans[0] > id:
                    ans = (id, time)
        return ans[0]


n = 10
logs = [[0,3],[2,5],[0,9],[1,15]]

n = 26
logs = [[1,1],[3,7],[2,12],[7,17]]

n = 2
logs = [[0,10],[1,20]]

solution = Solution()
print(solution.hardestWorker(n, logs))
