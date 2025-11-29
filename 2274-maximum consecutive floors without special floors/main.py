class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        # pre-process
        special = sorted(special)
        L = len(special)

        # process
        ans = 0
        idx = 0
        prev = bottom
        while idx < L:
            ans = max(ans, special[idx] - prev)
            prev = special[idx] + 1
            idx += 1
        ans = max(ans, top - prev + 1)
        return ans


bottom = 2
top = 9
special = [4,6]

bottom = 6
top = 8
special = [7,6,8]

solution = Solution()
print(solution.maxConsecutive(bottom, top, special))
