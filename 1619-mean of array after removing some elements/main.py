class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        # pre-process
        L = len(arr)
        arr = sorted(arr)

        # process
        start = int(L * 0.05)
        end = int(L * 0.95)
        total = 0
        for x in range(start, end):
            total += arr[x]
        ans = total / (L * 0.9)
        return ans


arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]

solution = Solution()
print(solution.trimMean(arr))
