class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        # helper function
        def remove(nums):
            from heapq import heapify, heappush, heappop
            heap = list()
            heapify(heap)

            idx = 0
            while idx < len(nums) - 1:
                heappush(heap, (nums[idx] + nums[idx + 1], idx))
                idx += 1
            target, target_idx = heappop(heap)
            processed = list()
            idx = 0
            while idx < len(nums):
                if idx == target_idx:
                    processed.append(target)
                elif idx == target_idx + 1:
                    pass
                else:
                    processed.append(nums[idx])
                idx += 1
            return processed

        def nonDecreasing(nums):
            idx = 0
            while idx < len(nums) - 1:
                if nums[idx] > nums[idx + 1]:
                    return False
                idx += 1
            return True

        # process
        ans = 0
        while not nonDecreasing(nums):
            nums = remove(nums)
            ans += 1
        return ans


nums = [5,2,3,1]
nums = [1,2,2]

solution = Solution()
print(solution.minimumPairRemoval(nums))
