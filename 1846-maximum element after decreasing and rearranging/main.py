class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # pre-process
        L = len(arr)

        arr = sorted(arr)
        arr[0] = 1

        # process
        for x in range(1, L):
            if arr[x] > arr[x - 1]:
                arr[x] = arr[x - 1] + 1
        ans = arr[L - 1]

        return ans


arr = [2,2,1,2,1]
arr = [100,1,1000]
arr = [1,2,3,4,5]
arr = [100]
arr = [1000,100,10,1]

solution = Solution()
print(solution.maximumElementAfterDecrementingAndRearranging(arr))
