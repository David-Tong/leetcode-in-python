class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(arr)
        fractions = list()
        for x in range(L):
            for y in range(x + 1, L):
                fractions.append((arr[x] * 1.0 / arr[y], arr[x], arr[y]))

        # process
        fractions = sorted(fractions)
        _, x, y = fractions[k - 1]
        ans = [x, y]

        return ans


arr = [1,2,3,5]
k = 3

arr = [1, 7]
k = 1

solution = Solution()
print(solution.kthSmallestPrimeFraction(arr, k))
