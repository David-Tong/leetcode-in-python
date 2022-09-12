class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        L = len(arr)
        missings = [0] * L

        for idx, item in enumerate(arr):
            missings[idx] = item - (idx + 1)

        from bisect import bisect_left
        idx = bisect_left(missings, k) - 1
        if idx == -1:
            ans = k
        else:
            ans = arr[idx] + k - missings[idx]

        return ans


arr = [2,3,4,7,11]
k = 5

arr = [1,2,3,4]
k = 2

arr = [1]
k = 2

arr = [2]
k = 1

arr = [6, 10]
k = 5

solution = Solution()
print(solution.findKthPositive(arr, k))
