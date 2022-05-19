class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        from bisect import bisect_left
        idx = bisect_left(arr, x)

        left = idx - 1
        right = idx
        count = 0
        from collections import deque
        ans = deque()
        while left >= 0 and right < len(arr) and count < k:
            if x - arr[left] <= arr[right] - x:
                ans.appendleft(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
            count += 1

        while left >= 0 and count < k:
            ans.appendleft(arr[left])
            left -= 1
            count += 1

        while right < len(arr) and count < k:
            ans.append(arr[right])
            right += 1
            count += 1

        return ans


arr = [1,2,3,4,5]
k = 4
x = 3

arr = [1,2,3,4,5]
k = 4
x = 7

arr = [2,2,2,2,2]
k = 3
x = 2

solution = Solution()
print(solution.findClosestElements(arr, k, x))
