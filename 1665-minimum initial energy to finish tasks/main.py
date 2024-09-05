class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks = sorted(tasks, key=lambda x: (x[0] - x[1], x[1] * -1))

        def canFinish(energy):
            for task in tasks:
                if energy < task[1]:
                    return False
                energy -= task[0]
            return True

        left = 1
        right = 10 ** 9

        while left + 1 < right:
            middle = (left + right) // 2
            if canFinish(middle):
                right = middle
            else:
                left = middle + 1

        if canFinish(left):
            return left
        else:
            return right


tasks = [[1,2],[2,4],[4,8]]
tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
tasks = [[1,6]]
tasks = [[1,22],[1,18],[6,11],[5,14],[2,6],[7,9]]

solution = Solution()
print(solution.minimumEffort(tasks))
