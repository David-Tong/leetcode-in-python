class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        # process
        curr = 0
        ans = 0
        for rung in rungs:
            if curr + dist < rung:
                r = (rung - curr) // dist
                if (rung - curr) % dist == 0:
                    r -= 1
                ans += r
            curr = rung
        return ans


rungs = [1,3,5,10]
dist = 2

rungs = [3,6,8,10]
dist = 3

rungs = [3,4,6,7]
dist = 2

rungs = [846396320,857701623,965011303,992835584,998444246,999450293,999830155,999848086,999896122,999898715,999899241,999899401,999899876,999900004,999900005,999900013,999900014,999900017,999900019,999900020]
dist = 1

rungs = [12, 24]
dist = 4

solution = Solution()
print(solution.addRungs(rungs, dist))
