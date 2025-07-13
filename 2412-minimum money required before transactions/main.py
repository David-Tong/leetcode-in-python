class Solution(object):
    def minimumMoney(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        # pre-process
        maxi_money = 0
        losses = list()
        for transaction in transactions:
            money, cost = transaction
            gain = cost - money
            if gain >= 0:
                maxi_money = max(maxi_money, money)
            else:
                losses.append(transaction)
        losses = sorted(losses, key=lambda x: x[1])
        # print(maxi_money)
        # print(losses)

        # process
        ans = maxi_money
        L = len(losses)
        for x in range(L - 1, -1, -1):
            money, cost = losses[x]
            if x == L - 1:
                ans += money
                if maxi_money > 0:
                    ans -= min(cost, maxi_money)
            else:
                ans -= cost
                ans += money
        return ans


transactions = [[2,1],[5,0],[4,2]]
transactions = [[3,0],[0,3]]
transactions = [[7,2],[0,10],[5,0],[4,1],[5,8],[5,9]]
transactions = [[2,1],[5,0],[4,2],[0,1]]
transactions = [[2,1],[5,0],[4,2],[0,2]]
transactions = [[2,1],[5,0],[4,2],[0,3]]

solution = Solution()
print(solution.minimumMoney(transactions))
