class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        up_down = 0
        stack = []
        stack.append(prices[0])
        ans = 0
        for price in prices[1:]:
            if price > stack[-1]:
                if up_down == 1:
                    stack.pop(-1)
                else:
                    up_down = 1
                stack.append(price)
            elif price < stack[-1]:
                if up_down == 1:
                    high = stack.pop(-1)
                    low = stack.pop(-1)
                    ans += high - low
                else:
                    stack.pop(-1)
                stack.append(price)
                up_down = -1

        if len(stack) == 2:
            high = stack.pop(-1)
            low = stack.pop(-1)
            ans += high - low

        return ans


prices = [7, 1, 5, 3, 6, 4]
prices = [1, 2, 3, 4, 5]
prices = [7, 6, 4, 3, 1]
prices = [1, 1]
prices = [1]
prices = [3, 1, 0, 5, 9, 7, 2, 3, 4, 11]

solution = Solution()
print(solution.maxProfit(prices))
