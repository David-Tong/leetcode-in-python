class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # pre-process
        def doSum(num):
            total = 0
            for digit in num:
                total += int(digit)
            return total

        # process
        ans = 0
        for num in range(low, high + 1):
            num = str(num)
            if len(num) % 2 == 0:
                half = len(num) // 2
                if doSum(num[:half]) == doSum(num[half:]):
                    ans += 1
        return ans


low = 1
high = 100

low = 1200
high = 1230

solution = Solution()
print(solution.countSymmetricIntegers(low, high))
