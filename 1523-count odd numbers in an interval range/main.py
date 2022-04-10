class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = 0
        if low == high:
            if low % 2 == 1:
                ans = 1
        else:
            if low % 2 == 0:
                if high % 2 == 0:
                    ans = (high - low) // 2
                else:
                    ans = (high - low) // 2 + 1
            else:
                ans = (high - low) // 2 + 1
        return ans


low = 3
high = 7

low = 3
high = 6

low = 3
high = 3

solution = Solution()
print(solution.countOdds(low, high))
