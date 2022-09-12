class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def radixSort(nums):
            R = len(str(max(nums)))
            nums = [str(num) for num in nums]
            buckets = [[] for _ in range(10)]
            radix = 1
            while radix <= R:
                for num in nums:
                    if len(num) >= radix:
                        bucket = int(num[-1 * radix])
                        buckets[bucket].append(num)
                    else:
                        buckets[0].append(num)
                nums = []
                for idx, bucket in enumerate(buckets):
                    nums.extend(bucket)
                    buckets[idx] = []
                radix += 1
            return nums

        if len(nums) == 0:
            return 0

        negatives = []
        positives = []
        for num in nums:
            if num < 0:
                negatives.append(-1 * num)
            else:
                positives.append(num)

        if len(positives) > 0:
            positives = radixSort(positives)
            positives = [int(positive) for positive in positives]
        if len(negatives) > 0:
            negatives = radixSort(negatives)
            negatives = [-1 * int(negative) for negative in negatives[::-1]]

        nums = negatives + positives

        # get max consecutive sequence length
        left = 0
        right = 0
        ans = 1
        while right < len(nums):
            if right > 0:
                if nums[right] - nums[right - 1] <= 1:
                    if right == len(nums) - 1:
                        ans = max(ans, nums[right] - nums[left] + 1)
                else:
                    ans = max(ans, nums[right - 1] - nums[left] + 1)
                    left = right
            right += 1
        return ans


nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
#nums = [100,4,200,1,3,2,101,5,107,106,105,102,103,104]
nums = [-2,8,-1,0,1,2,7,9,10,11,12,-3,-4,-5]

#nums = [0,3,2,4,6,0,1,1,2,3,7,8,9,10,11,12,12,13]
#nums = []
#nums = [0]
nums = [0, -1]

solution = Solution()
print(solution.longestConsecutive(nums))
