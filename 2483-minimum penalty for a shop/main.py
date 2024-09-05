class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        L = len(customers)
        opens = [0] * (L + 1)
        closes = [0] * (L + 1)

        for idx, customer in enumerate(customers):
            if customer == "Y":
                opens[idx + 1] = opens[idx] + 1
                closes[idx + 1] = closes[idx]
            elif customer == "N":
                opens[idx + 1] = opens[idx]
                closes[idx + 1] = closes[idx] + 1

        mini = float("inf")
        ans = -1
        for x in range(L + 1):
            lost = opens[-1] - opens[x] + closes[x]
            if mini > lost:
                mini = lost
                ans = x
        return ans


customers = "YYNY"
customers = "NNNNN"
customers = "YYYYY"

solution = Solution()
print(solution.bestClosingTime(customers))
