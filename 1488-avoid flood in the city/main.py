class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        L = len(rains)
        ans = [-1] * L

        drys = list()
        for idx, rain in enumerate(rains):
            if rain == 0:
                drys.append(idx)

        from collections import defaultdict
        lakes = defaultdict(int)

        from bisect import bisect_right
        for idx, rain in enumerate(rains):
            if rain != 0:
                if rain not in lakes:
                    lakes[rain] = idx
                else:
                    idx2 = bisect_right(drys, lakes[rain])
                    if idx2 < len(drys) and lakes[rain] < drys[idx2] < idx:
                        ans[drys[idx2]] = rain
                        lakes[rain] = idx
                        drys.remove(drys[idx2])
                    else:
                        return list()

        for dry in drys:
            ans[dry] = 1

        return ans


rains = [1,2,3,4]
rains = [1,2,0,0,2,1]
rains = [1,2,0,1,2]
rains = [0,1,1]
#rains = [1,0,2,0,2,1]
#rains = [1,0,2,3,0,1,2]
rains = [1,1,0,0]

solution = Solution()
print(solution.avoidFlood(rains))
