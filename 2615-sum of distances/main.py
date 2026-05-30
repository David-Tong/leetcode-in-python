class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, num in enumerate(nums):
            dicts[num].append(idx)

        distances = defaultdict(int)
        for num in dicts:
            idx = dicts[num][0]
            for idx2 in dicts[num][1:]:
                distances[num] += idx2 - idx
        # print(distances)

        # process
        ans = [0] * L
        for num in dicts:
            idx = 0
            while idx < len(dicts[num]):
                idx2 = dicts[num][idx]
                if idx == 0:
                    ans[idx2] = distances[num]
                else:
                    # root shift method
                    shift = idx2 - dicts[num][idx - 1]
                    left = idx
                    right = len(dicts[num]) - idx
                    ans[idx2] = distances[num] + (left - right) * shift
                    distances[num] = ans[idx2]
                idx += 1
        return ans


nums = [1,3,1,1,2]
nums = [0,5,3]
nums = [1] * 10 ** 5
print(nums)

solution = Solution()
print(solution.distance(nums))
