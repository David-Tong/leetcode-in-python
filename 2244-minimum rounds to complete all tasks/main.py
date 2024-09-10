class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        from collections import defaultdict
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1

        from math import ceil
        ans = 0
        for key in counts:
            if counts[key] == 1:
                return -1
            ans += ceil(counts[key] / 3.0)
        return int(ans)


tasks = [2,2,3,3,2,4,4,4,4,4]
tasks = [2,3,3]

solution = Solution()
print(solution.minimumRounds(tasks))
