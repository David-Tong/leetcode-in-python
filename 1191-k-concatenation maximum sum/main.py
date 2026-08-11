class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7

        # helper function
        def getMaxSum(arr):
            if k > 1:
                arr = arr * 2
            idx = 0
            res = 0
            presum = 0
            while idx < len(arr):
                presum = max(0, presum + arr[idx])
                res= max(res, presum)
                idx += 1
            return res

        # print(getMaxSum(arr))

        # process
        maxi = getMaxSum(arr)
        total = sum(arr)
        if total > 0:
            if k > 2:
                ans = maxi + total * (k - 2)
            else:
                ans = maxi
        else:
            ans = maxi
        ans = ans % MODULO
        return ans


arr = [1,2]
k = 3

arr = [1,-2,1]
k = 5

arr = [-1,-2]
k = 7

arr = [1,2,-3,-3,2,1]
k = 3

arr = [-5,-2,0,0,3,9,-2,-5,4]
k = 5

arr = [1, 2]
k = 1

"""
from random import randint
arr = [randint(-10 ** 4, 10 ** 4) for _ in range(10 ** 5)]
print(arr)
k = 10 ** 4
"""

solution = Solution()
print(solution.kConcatenationMaxSum(arr, k))
