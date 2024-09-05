class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        # pre-process
        L = len(fronts)

        # search
        candidates = set()
        for x in range(L):
            candidates.add(fronts[x])
            candidates.add(backs[x])

        for x in range(L):
            if fronts[x] == backs[x]:
                if fronts[x] in candidates:
                    candidates.remove(fronts[x])

        return min(candidates) if candidates else 0


fronts = [1,2,4,4,7]
backs = [1,3,4,1,3]

fronts = [1]
backs = [1]

fronts = [1,1,1,1,1]
backs = [2,2,2,2,2]

fronts = [1,2]
backs = [2,1]

fronts = [1,1]
backs = [2,2]

fronts = [1,1]
backs = [1,1]

fronts = [2,2,2,2,1]
backs = [2,1,2,1,1]

solution = Solution()
print(solution.flipgame(fronts, backs))
