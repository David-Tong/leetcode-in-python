class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        # pre-process
        L = len(arr)
        arr = sorted(arr)
        mini = float("inf")
        for x in range(L - 1):
            mini = min(mini, arr[x + 1] - arr[x])

        # process
        ans = list()
        for x in range(L - 1):
            if arr[x + 1] - arr[x] == mini:
                ans.append([arr[x], arr[x + 1]])
        return ans


arr = [4,2,1,3]
arr = [1,3,6,10,15]
arr = [3,8,-10,23,19,-4,-14,27]

solution = Solution()
print(solution.minimumAbsDifference(arr))
