class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        # pre-process
        fibonaccis = [1, 1]
        fibonacci = 0
        while fibonacci <= k:
            fibonacci = fibonaccis[-1] + fibonaccis[-2]
            fibonaccis.append(fibonacci)

        # process
        from bisect import bisect_right
        target = k
        ans = 0
        while target > 0:
            idx = bisect_right(fibonaccis, target)
            target -= fibonaccis[idx - 1]
            ans += 1
        return ans


k = 7
k = 10
k = 19
k = 10 ** 9

solution = Solution()
print(solution.findMinFibonacciNumbers(k))