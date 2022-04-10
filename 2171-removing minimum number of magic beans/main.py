class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans = sorted(beans)
        prefixes = [0] * (len(beans) + 1)
        for x in range(len(beans) + 1):
            if x == 0:
                prefixes[x] = 0
            else:
                prefixes[x] = prefixes[x - 1] + beans[x - 1]

        ans = float("inf")
        for x in range(1, len(prefixes)):
            removes = (prefixes[len(prefixes) - 1] - prefixes[x - 1]) - (beans[x - 1] * (len(prefixes) - x)) + prefixes[x - 1]
            ans = min(ans, removes)

        return ans


beans = [4, 1, 6, 5]
beans = [2, 10, 3, 2]
beans = [1]

solution = Solution()
print(solution.minimumRemoval(beans))
