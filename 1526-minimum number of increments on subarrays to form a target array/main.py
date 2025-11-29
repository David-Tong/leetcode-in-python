class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        # pre-process
        L = len(target)

        # process
        ans = target[0]
        for x in range(1, L):
            ans += max(0, target[x] - target[x - 1])
        return ans


target = [1,2,3,2,1]
target = [3,1,1,2]
target = [3,1,5,4,2]

solution = Solution()
print(solution.minNumberOperations(target))
