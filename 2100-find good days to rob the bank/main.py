class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        # pre-process
        L = len(security)

        # from left to right, search for non-increasing subarray
        idx = 1
        decreasing = [0] * L
        while idx < L:
            if security[idx] <= security[idx - 1]:
                decreasing[idx] = decreasing[idx - 1] + 1
            else:
                decreasing[idx] = 0
            idx += 1
        # print(decreasing)

        # from right to left, search for non-decreasing subarray
        idx = L - 2
        increasing = [0] * L
        while idx >= 0:
            if security[idx] <= security[idx + 1]:
                increasing[idx] = increasing[idx + 1] + 1
            else:
                increasing[idx] = 0
            idx -= 1
        # print(increasing)

        # process
        idx = time
        ans = list()
        while idx < L - time:
            if decreasing[idx] >= time and increasing[idx] >= time:
                ans.append(idx)
            idx += 1
        return ans


security = [5,3,3,3,5,6,2]
time = 2

security = [1,1,1,1,1]
time = 0

security = [1,1,1,1,1]
time = 1

security = [1,2,3,4,5,6]
time = 2

security = [1,2,3,4,5,4,3,2,1]
time = 2

security = [5,4,3,2,1,2,3,4,5]
time = 2

solution = Solution()
print(solution.goodDaysToRobBank(security, time))
