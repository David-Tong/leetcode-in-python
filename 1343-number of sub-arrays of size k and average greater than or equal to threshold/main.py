class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        # pre-process
        L = len(arr)
        presums = [0]
        for num in arr:
            presums.append(presums[-1] + num)

        # process
        left = 0
        right = left + k
        ans = 0
        while right <= L:
            total = presums[right] - presums[left]
            if total >= threshold * k:
                ans += 1
            left += 1
            right = left + k
        return ans


arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5

arr = [1]
k = 1
threshold = 1

from random import randint
arr = [randint(1, 10 ** 4) for _ in range(10 ** 5)]
k = 20
threshold = 1500
print(arr)

solution = Solution()
print(solution.numOfSubarrays(arr, k, threshold))
