class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from sortedcontainers import SortedList
        sorted_list = SortedList()
        idxes = SortedList()
        reversal = 0
        for x in range(L - 1):
            sorted_list.add((nums[x] + nums[x + 1], x))
            idxes.add(x)
            if nums[x] > nums[x + 1]:
                reversal += 1
        idxes.add(L - 1)

        # process
        ans = 0
        while reversal > 0:
            # fetch the pair with the minimum sum
            delta = 0
            total, idx = sorted_list.pop(0)
            mapped_idx = idxes.bisect_left(idx)
            # process
            # previous pair
            if mapped_idx > 0:
                prev_idx = idxes[mapped_idx - 1]
                prev = (nums[prev_idx] + nums[idx], prev_idx)
                if nums[prev_idx] > nums[idx]:
                    delta -= 1
                if nums[prev_idx] > total:
                    delta += 1
                sorted_list.remove(prev)
                sorted_list.add((nums[prev_idx] + total, prev_idx))
            # next pair
            nxt_idx = idxes[mapped_idx + 1]
            if mapped_idx < len(idxes) - 2:
                nxt_nxt_idx = idxes[mapped_idx + 2]
                nxt = (nums[nxt_idx] + nums[nxt_nxt_idx], nxt_idx)
                if nums[nxt_idx] > nums[nxt_nxt_idx]:
                    delta -= 1
                if total > nums[nxt_nxt_idx]:
                    delta += 1
                sorted_list.remove(nxt)
                sorted_list.add((total + nums[nxt_nxt_idx], idx))
            # update new pair
            if nums[idx] > nums[nxt_idx]:
                delta -= 1
            nums[idx] = total
            # print(sorted_list)
            # update
            reversal += delta
            idxes.remove(nxt_idx)
            ans += 1
        return ans


nums = [5,2,3,1]
nums = [1,2,2]

from random import randint
nums = [randint(-10 ** 4, 10 ** 4) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.minimumPairRemoval(nums))
