class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # pre-process
        N = len(arr)
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, num in enumerate(arr):
            dicts[num].append(idx)

        # process
        # helper function
        def process(idxes):
            L = len(idxes)
            idx = 1
            distance = 0
            while idx < L:
                distance += idxes[idx] - idxes[0]
                idx += 1

            distances = list()
            distances.append(distance)
            idx = 1
            while idx < L:
                left, right = idx, L - idx
                shift = idxes[idx] - idxes[idx - 1]
                distance = distance + left * shift - right * shift
                distances.append(distance)
                idx += 1
            return distances

        ans = [0] * N
        for num in dicts:
            idxes = dicts[num]
            distances = process(idxes)
            idx = 0
            while idx < len(idxes):
                ans[idxes[idx]] = distances[idx]
                idx += 1
        return ans


arr = [2,1,3,1,2,3,3]
arr = [10,5,10,10]

from random import randint
arr = [randint(1, 100) for _ in range(10 ** 4)]
print(arr)

solution = Solution()
print(solution.getDistances(arr))
