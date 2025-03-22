class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(prices)

        # process
        from copy import deepcopy
        ans = deepcopy(prices)
        for x in range(L):
            for y in range(x + 1, L):
                if prices[x] >= prices[y]:
                    ans[x] = prices[x] - prices[y]
                    break
        return ans


prices = [8,4,6,2,3]
prices = [1,2,3,4,5]
prices = [10,1,1,6]
prices = [5,4,3,2,1]
prices = [1]
prices = [8,7,4,2,8,1,7,7,10,1]

solution = Solution()
print(solution.finalPrices(prices))
