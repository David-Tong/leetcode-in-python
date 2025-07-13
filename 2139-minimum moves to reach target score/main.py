class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        # process
        ans = 0
        while target != 1 and maxDoubles > 0:
            if target & 1:
               ans += 1
            target >>= 1
            ans += 1
            maxDoubles -= 1

        ans += target - 1
        return ans


target = 5
maxDoubles = 0

target = 19
maxDoubles = 2

target = 10
maxDoubles = 4

solution = Solution()
print(solution.minMoves(target, maxDoubles))
