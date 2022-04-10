class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        for x in range(1, len(arr)):
            if diff != arr[x] - arr[x-1]:
                return False
        return True


arr = [3, 5, 1]
arr = [1, 2, 4]
#arr = [1, -1, 0]


solution = Solution()
print(solution.canMakeArithmeticProgression(arr))
