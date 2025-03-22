class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        # process
        days = 1
        for task in tasks:
            if task in dicts:
                if days - dicts[task] <= space:
                    days = dicts[task] + space + 1
            dicts[task] = days
            days += 1
        ans = days - 1
        return ans


tasks = [1,2,1,2,3,1]
space = 3

tasks = [5,8,8,5]
space = 2

solution = Solution()
print(solution.taskSchedulerII(tasks, space))
