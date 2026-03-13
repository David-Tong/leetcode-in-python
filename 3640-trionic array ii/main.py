class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # print(nums)
        presums = [0]
        for x in range(L):
            presums.append(presums[-1] + nums[x])
        # print(presums)

        increasings, decreasings = list(), list()
        idx = 0
        start = 0
        increasing = True
        while idx < L - 1:
            if nums[idx] == nums[idx + 1]:
                if increasing:
                    if idx > start:
                        increasings.append((start, idx))
                else:
                    if idx > start:
                        decreasings.append((start, idx))
                start = idx + 1
            elif nums[idx] < nums[idx + 1]:
                if not increasing:
                    if idx > start:
                        decreasings.append((start, idx))
                    start = idx
                    increasing = True
            else:
                if increasing:
                    if idx > start:
                        increasings.append((start, idx))
                    start = idx
                    increasing = False
            idx += 1
        if increasing:
            if idx > start:
                increasings.append((start, L - 1))
        else:
            if idx > start:
                decreasings.append((start, L - 1))

        # print(increasings)
        # print(decreasings)

        from collections import defaultdict
        increasings_dict = defaultdict(list)
        decreasings_dict = defaultdict(list)

        for increasing in increasings:
            increasings_dict[increasing[0]].append(increasing[1])
            idx = increasing[0]
            flag = False
            while idx <= increasing[1]:
                if nums[idx] <= 0:
                    idx += 1
                else:
                    flag = True
                    if idx == increasing[1]:
                        idx -= 1
                    increasings_dict[increasing[0]].append(idx)
                    break
            if not flag:
                increasings_dict[increasing[0]].append(increasing[1] - 1)
            idx = increasing[0] + 1
            while idx <= increasing[1]:
                if presums[idx + 1] - presums[increasing[0]] < presums[increasing[1] + 1] - presums[increasing[0]]:
                    idx += 1
                else:
                    increasings_dict[increasing[0]].append(idx)
                    break

        for decreasing in decreasings:
            decreasings_dict[decreasing[0]].append(decreasing[1])

        # print(increasings_dict)
        # print(decreasings_dict)

        # process
        ans = float('-inf')
        for idx in increasings_dict:
            idx2 = increasings_dict[idx][0]
            if idx2 in decreasings_dict:
                idx3 = decreasings_dict[idx2][0]
                if idx3 in increasings_dict:
                    start = increasings_dict[idx][1]
                    end = increasings_dict[idx3][2]
                    # print(start, end)
                    total = presums[end + 1] - presums[start]
                    ans = max(ans, total)
        return ans


nums = [0,-2,-1,-3,0,2,-1]
nums = [1,4,2,7]
nums = [0,-2,-1,1,-30,-19,-18,-17,0,2,-1]

from random import randint
nums = [randint(-10 ** 3, 10 ** 3) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.maxSumTrionic(nums))
