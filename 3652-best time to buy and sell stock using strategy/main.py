class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(prices)
        ans = sum([x * y for x, y in zip(prices, strategy)])

        profit = 0
        for x in range(L):
            if x < k // 2:
                pass
            elif x < k:
                profit += prices[x]
            else:
                profit += strategy[x] * prices[x]

        # process
        ans = max(ans, profit)
        for x in range(L - k):
            # the element move out
            profit += strategy[x] * prices[x]
            # the element move in
            profit -= strategy[x + k] * prices[x + k]
            profit += prices[x + k]
            # the element in the middle get changed
            profit -= prices[x + k // 2]
            ans = max(ans, profit)
        return ans


prices = [4,2,8]
strategy = [-1,0,1]
k = 2

prices = [5,4,3]
strategy = [1,1,0]
k = 2

solution = Solution()
print(solution.maxProfit(prices, strategy, k))
