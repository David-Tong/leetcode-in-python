class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        # pre-process
        L = len(startTime)
        start = 0
        total = 0

        for x in range(k):
            total += endTime[x] - startTime[x]

        # process
        ans = 0
        for x in range(k, L):
            ans = max(ans, startTime[x] - total - start)
            start = endTime[x - k]
            total -= endTime[x - k] - startTime[x - k]
            total += endTime[x] - startTime[x]
        ans = max(ans, eventTime - total - start)
        return ans


eventTime = 5
k = 1
startTime = [1,3]
endTime = [2,5]

eventTime = 10
k = 1
startTime = [0,2,9]
endTime = [1,4,10]

eventTime = 5
k = 2
startTime = [0,1,2,3,4]
endTime = [1,2,3,4,5]

solution = Solution()
print(solution.maxFreeTime(eventTime, k, startTime, endTime))
