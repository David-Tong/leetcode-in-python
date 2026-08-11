class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        # pre-process
        # calculate cost
        def cost(cooking):
            current = startAt
            res= 0
            for digit in str(int(cooking)):
                digit = int(digit)
                if digit != current:
                    res += moveCost
                res += pushCost
                current = digit
            return res

        # process
        ans = float('inf')
        minutes = targetSeconds // 60
        seconds = targetSeconds % 60

        if minutes < 100:
            if seconds < 10:
                cooking = str(minutes) + "0" + str(seconds)
            else:
                cooking = str(minutes) + str(seconds)
            ans = min(ans, cost(cooking))

        if 0 <= seconds < 40:
            if minutes > 0:
                cooking = str(minutes - 1) + str(seconds + 60)
                ans = min(ans, cost(cooking))

        return ans


startAt = 1
moveCost = 2
pushCost = 1
targetSeconds = 600

startAt = 0
moveCost = 1
pushCost = 2
targetSeconds = 76

startAt = 0
moeCost = 1
pushCost = 4
targetSeconds = 9

startAt = 1
moveCost = 9403
pushCost = 9402
targetSeconds = 6008

solution = Solution()
print(solution.minCostSetTime(startAt, moveCost, pushCost, targetSeconds))
