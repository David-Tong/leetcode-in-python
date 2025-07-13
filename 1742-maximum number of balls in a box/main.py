class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        # pre-process
        # getBox - get the box of the ball with the num
        def getBox(num):
            ans = 0
            for d in str(num):
                ans += int(d)
            return ans

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        for num in range(lowLimit, highLimit + 1):
            dicts[getBox(num)] += 1

        ans = max(dicts.values())
        return ans


lowLimit = 1
highLimit = 10

lowLimit = 5
highLimit = 15

lowLimit = 19
highLimit = 28

solution = Solution()
print(solution.countBalls(lowLimit, highLimit))
