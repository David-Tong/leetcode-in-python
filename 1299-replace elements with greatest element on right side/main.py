class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(arr)

        # process
        ans = list()
        ans.append(-1)
        idx = L - 1
        maxi = float("-inf")
        while idx >= 0:
            maxi = max(maxi, arr[idx])
            ans.append(maxi)
            idx -= 1
        ans.pop()
        ans = ans[::-1]
        return ans


arr = [17,18,5,4,6,1]
arr = [400]

solution = Solution()
print(solution.replaceElements(arr))
