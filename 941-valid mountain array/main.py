class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False

        left = 0
        right = len(arr) - 1

        while left < len(arr) - 1:
            if arr[left] < arr[left + 1]:
                left += 1
            else:
                break

        while right > 0:
            if arr[right] < arr[right - 1]:
                right -= 1
            else:
                break

        if left == len(arr) - 1 or right == 0 or left != right:
            return False
        else:
            return True


solution = Solution()
arrs = [[2, 1], [3, 5, 5], [0, 3, 2, 1]]
for arr in arrs:
    print(solution.validMountainArray(arr))
