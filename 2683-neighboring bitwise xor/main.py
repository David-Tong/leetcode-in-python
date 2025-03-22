class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        # process
        start = 0
        xor = start
        for drv in derived:
            xor ^= drv

        return start == xor


derived = [1,1,0]
derived = [1,1]
derived = [1,0]

solution = Solution()
print(solution.doesValidArrayExist(derived))
