class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        from sortedcontainers import SortedList
        unvisited = SortedList()
        for idx, num in enumerate(nums):
            unvisited.add((idx, num))

        # help function
        def search(start):
            group = list()
            maxi = 0

            # bfs
            from collections import deque
            bfs = deque()
            bfs.append(start)
            group.append(unvisited[start][0])
            maxi = max(maxi, unvisited[start][1])
            unvisited.pop(start)

            while bfs:
                curr = bfs.popleft()
                pivot = unvisited.bisect_left((curr, nums[curr]))
                # condition 2
                # jump to index j where j < i is allowed only if nums[j] > nums[i]
                idx = pivot - 1
                while idx >= 0:
                    if unvisited[idx][1] > nums[curr]:
                        bfs.append(unvisited[idx][0])
                        group.append(unvisited[idx][0])
                        maxi = max(maxi, unvisited[idx][1])
                        unvisited.pop(idx)
                    idx -= 1

                # condition 1
                # jump to index j where j > i is allowed only if nums[j] < nums[i]
                idx = pivot
                while idx < len(unvisited):
                    if unvisited[idx][1] < nums[curr]:
                        bfs.append(unvisited[idx][0])
                        group.append(unvisited[idx][0])
                        maxi = max(maxi, unvisited[idx][1])
                        unvisited.pop(idx)
                    idx += 1
            return group, maxi

        # process
        ans = [0] * L
        while len(unvisited) > 0:
            group, maxi = search(0)
            print(len(group))
            for idx in group:
                ans[idx] = maxi
        return ans


nums = [2,1,3]
nums = [2,3,1]
nums = [30,21,5,35,24]
nums = [9,30,16,6,36,9]
nums = [1,1,1,1,1]

from random import randint
nums = [randint(1, 10 ** 3) for _ in range(10 ** 4)]
print(nums)

solution = Solution()
print(solution.maxValue(nums))
