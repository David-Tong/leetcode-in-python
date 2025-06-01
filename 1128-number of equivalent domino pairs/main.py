class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        # pre-process
        def getKey(dominoe):
            num, num2 = dominoe[0], dominoe[1]
            if num < num2:
                num, num2 = num2, num
            return "{}-{}".format(num, num2)

        # process
        from collections import defaultdict
        dicts = defaultdict(int)
        for dominoe in dominoes:
            dicts[getKey(dominoe)] += 1

        # post-process
        ans = 0
        for key in dicts:
            if dicts[key] > 1:
                pairs = dicts[key]
                ans += pairs * (pairs - 1) // 2
        return ans


dominoes = [[1,2],[2,1],[3,4],[5,6]]
dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
dominoes = [[1,2],[1,2],[3,1],[1,2],[1,3]]

solution = Solution()
print(solution.numEquivDominoPairs(dominoes))
