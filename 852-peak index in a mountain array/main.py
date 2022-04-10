class Solution(object):
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left + 1 < right:
            middle = (left + right) // 2
            if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
                return middle
            elif arr[middle] > arr[middle - 1]:
                left = middle
            else:
                right = middle

        if arr[left] > arr[right]:
            return left
        else:
            return right


arr = [0,1,0]
arr = [0,2,1,0]
arr = [0,10,5,2]
solution = Solution()
print(solution.peakIndexInMountainArray(arr))