class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2 = sorted(arr2)
        from bisect import bisect_left, bisect_right

        ans = 0
        for item in arr1:
            left = item - d
            right = item + d
            idx_left = bisect_left(arr2, left)
            idx_right = bisect_right(arr2, right)
            if idx_left == idx_right:
                ans += 1

        return ans


arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2

arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3

arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6

solution = Solution()
print(solution.findTheDistanceValue(arr1, arr2, d))
