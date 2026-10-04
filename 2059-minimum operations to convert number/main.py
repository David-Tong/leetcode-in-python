class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        # process
        operators = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x ^ y]

        from collections import deque
        bfs = deque()
        bfs.append(start)
        visited = set()
        visited.add(start)

        steps = 1
        while bfs:
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                if 0 <= curr <= 1000:
                    for num in nums:
                         for operator in operators:
                            nxt = operator(curr, num)
                            if nxt == goal:
                                return steps
                            if nxt not in visited:
                                bfs.append(nxt)
                                visited.add(nxt)
            steps += 1
        return -1


nums = [2,4,12]
start = 2
goal = 12

nums = [3,5,7]
start = 0
goal = -4

nums = [2,8,16]
start = 0
goal = 1

from random import randint
nums = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
start = 500
goal = range(0, 10 ** 5)

solution = Solution()
print(solution.minimumOperations(nums, start, goal))
