class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        L = len(arr)

        # find the right non-decreasing array
        y = L - 1
        while y > 0 and arr[y] >= arr[y - 1]:
            y -= 1
        if y == 0:
            return 0

        ans = min(L - 1, y)
        for x in range(L):
            # search the left non-decreasing array
            if x == 0 or (x > 0 and arr[x] >= arr[x - 1]):
                while y < L and arr[x] > arr[y]:
                    y += 1
                ans = min(ans, y - x - 1)
            else:
                break
        return ans


arr = [1,2,3,10,4,2,3,5]
arr = [5,4,3,2,1]
arr = [1,2,3]
arr = [16,10,0,3,22,1,14,7,1,12,15]

solution = Solution()
print(solution.findLengthOfShortestSubarray(arr))
