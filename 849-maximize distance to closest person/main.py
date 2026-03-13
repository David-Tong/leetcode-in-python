class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # pre-process
        L = len(seats)
        lefts = [-1]
        for x in range(L):
            if seats[x] == 1:
                lefts.append(x)
            else:
                lefts.append(lefts[-1])
        rights = [-1]
        for x in range(L - 1, -1, -1):
            if seats[x] == 1:
                rights.append(x)
            else:
                rights.append(rights[-1])
        rights.reverse()
        # print(lefts)
        # print(rights)

        # process
        ans = 0
        for x in range(L):
            if lefts[x] == -1:
                ans = max(ans, rights[x] - x)
            elif rights[x] == -1:
                ans = max(ans, x - lefts[x])
            else:
                ans = max(ans, min(x - lefts[x], rights[x] - x))
        return ans


seats = [1,0,0,0,1,0,1]
seats = [1,0,0,0]
seats = [0,1]

solution = Solution()
print(solution.maxDistToClosest(seats))
