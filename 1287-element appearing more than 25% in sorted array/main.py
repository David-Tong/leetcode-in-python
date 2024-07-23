class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        L = len(arr)
        Q = L // 4

        for x in range(L - Q):
            if arr[x] == arr[x + Q]:
                return arr[x]


arr = [1,2,2,6,6,6,6,7,10]
arr = [1,1]
arr = [1,2,2,2,2,4,5,6,7,8,9,10,11]

solution = Solution()
print(solution.findSpecialInteger(arr))
