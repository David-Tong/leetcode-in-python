class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        L = len(profit)

        jobs = list()
        for x in range(L):
            jobs.append((startTime[x], endTime[x], profit[x]))
        jobs = sorted(jobs, key=lambda x:x[1])

        endTime = list()
        for x in range(L):
            endTime.append(jobs[x][1])

        dp = [0] * L
        dp[0] = jobs[0][2]

        from bisect import bisect_right
        for x in range(1, L):
            dp[x] = dp[x - 1]
            idx = bisect_right(endTime, jobs[x][0])
            if idx > 0:
                dp[x] = max(dp[x], dp[idx - 1] + jobs[x][2])
            else:
                dp[x] = max(dp[x], jobs[x][2])
        return dp[-1]


startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

startTime = [1,1,1]
endTime = [2,3,4]
profit = [5,6,4]

startTime = [6,15,7,11,1,3,16,2]
endTime = [19,18,19,16,10,8,19,8]
profit = [2,9,1,19,5,7,3,19]


solution = Solution()
print(solution.jobScheduling(startTime, endTime, profit))
