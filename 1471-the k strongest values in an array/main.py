class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(arr)
        arr = sorted(arr)

        # process
        left, right = 0, L - 1
        middle = (L - 1) // 2

        ans = list()
        count = 0
        while count < k:
            if arr[right] - arr[middle] >= arr[middle] - arr[left]:
                ans.append(arr[right])
                right -= 1
            else:
                ans.append(arr[left])
                left += 1
            count += 1
        return ans


arr = [1,2,3,4,5]
k = 2

arr = [1,1,3,5,5]
k = 2

arr = [6,7,11,7,6,8]
k = 5

from random import randint
arr = [randint(-10 ** 5,10 ** 5) for i in range(10 ** 5)]
k = 10 ** 5
print(arr)

solution = Solution()
print(solution.getStrongest(arr, k))
