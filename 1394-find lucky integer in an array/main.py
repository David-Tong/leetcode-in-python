class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # pre-process
        from collections import Counter
        counts = Counter(arr)

        # process
        ans = -1
        for num in counts:
            if num == counts[num]:
                ans = max(ans, num)
        return ans


arr = [2,2,3,4]
arr = [1,2,2,3,3,3]
arr = [2,2,2,3,3]

solution = Solution()
print(solution.findLucky(arr))
