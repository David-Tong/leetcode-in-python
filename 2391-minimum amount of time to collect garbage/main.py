class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        # pre-process
        presum = [0]
        for tvl in travel:
            presum.append(tvl + presum[-1])

        # process
        total_m, total_p, total_g = 0, 0, 0
        last_m, last_p, last_g = 0, 0, 0

        for idx, gbg in enumerate(garbage):
            for gg in gbg:
                if gg == "M":
                    total_m += 1
                    last_m = idx
                elif gg == "P":
                    total_p += 1
                    last_p = idx
                elif gg == "G":
                    total_g += 1
                    last_g = idx

        ans = total_m + total_p + total_g + presum[last_m] + presum[last_p] + presum[last_g]
        return ans


garbage = ["G","P","GP","GG"]
travel = [2,4,3]

garbage = ["MMM","PGM","GP"]
travel = [3,10]

solution = Solution()
print(solution.garbageCollection(garbage, travel))
