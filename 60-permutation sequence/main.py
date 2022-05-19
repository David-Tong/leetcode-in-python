class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = [str(_) for _ in range(1, n + 1)]

        def doPermutation(n, k, numbers):
            if k == 1:
                ans = "".join(numbers)
            else:
                from math import ceil, factorial
                idx = int(ceil(float(k) / factorial(n - 1))) - 1
                remain = k - factorial(n - 1) * idx
                ans = numbers[idx]
                ans += doPermutation(n - 1, remain, numbers[:idx] + numbers[idx + 1:])
            return ans

        return doPermutation(n, k, numbers)


n = 3
k = 3

n = 4
k = 9

n = 3
k = 1

n = 9
k = 5000

solution = Solution()
print(solution.getPermutation(n, k))
