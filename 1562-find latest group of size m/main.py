class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        # starts[x] = y - a group of 1 from x to y, included
        # ends[x] = y - a group of 1 from y to x, included
        from collections import defaultdict
        starts = defaultdict(int)
        ends = defaultdict(int)

        count = 0
        ans = -1
        for step, idx in enumerate(arr):
            # annex
            if idx + 1 in starts:
                if idx - 1 in ends:
                    # annex both left and right
                    starts[ends[idx - 1]] = starts[idx + 1]
                    ends[starts[idx + 1]] = ends[idx - 1]
                    # update count
                    if starts[idx + 1] - (idx + 1) + 1 == m:
                        count-= 1
                    if idx - 1 - ends[idx - 1] + 1 == m:
                        count -= 1
                    if starts[idx + 1] - (idx + 1) + (idx - 1) - ends[idx - 1] + 3 == m:
                        count += 1
                    # delete
                    del starts[idx + 1]
                    del ends[idx - 1]
                else:
                    # annex right
                    starts[idx] = starts[idx + 1]
                    ends[starts[idx + 1]] = idx
                    # update count
                    if starts[idx + 1] - (idx + 1) + 1 == m:
                        count -= 1
                    if starts[idx] - idx + 1 == m:
                        count += 1
                    # delete
                    del starts[idx + 1]
            else:
                if idx - 1 in ends:
                    # annex left
                    ends[idx] = ends[idx - 1]
                    starts[ends[idx - 1]] = idx
                    # update count
                    if (idx - 1) - ends[idx - 1] + 1 == m:
                        count -= 1
                    if idx - ends[idx] + 1 == m:
                        count += 1
                    # delete
                    del ends[idx - 1]
                else:
                    starts[idx] = idx
                    ends[idx] = idx
                    if m == 1:
                        count += 1
            if count > 0:
                ans = max(ans, step + 1)
        return ans


arr = [3,5,1,2,4]
m = 1

arr = [3,1,5,4,2]
m = 2

arr = [1,2,3,4,5]
m = 5

arr = [4,3,2,1]
m = 1

arr = [3,2,5,6,10,8,9,4,1,7]
m = 3

solution = Solution()
print(solution.findLatestStep(arr, m))
