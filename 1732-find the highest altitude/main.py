class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        L = len(gain)
        altitude = 0

        ans = 0
        for x in range(L):
            altitude += gain[x]
            ans = max(ans, altitude)
        return ans


gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]
gain = [-100]

solution = Solution()
print(solution.largestAltitude(gain))
