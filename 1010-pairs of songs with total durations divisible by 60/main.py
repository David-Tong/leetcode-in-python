class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # pre-process
        MODULO = 60
        from collections import defaultdict
        dicts = defaultdict(int)
        for t in time:
            mod = t % MODULO
            dicts[mod] += 1
        # print(dicts)

        # process
        ans = 0
        for mod in dicts:
            if mod == 0 or mod == 30:
                if dicts[mod] > 1:
                    ans += (dicts[mod] * (dicts[mod] - 1)) // 2
            elif mod < 30:
                if MODULO - mod in dicts:
                    ans += dicts[mod] * dicts[MODULO - mod]
        return ans


time = [30,20,150,100,40]
time = [60,60,60]

solution = Solution()
print(solution.numPairsDivisibleBy60(time))
