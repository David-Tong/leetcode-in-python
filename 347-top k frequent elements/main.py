class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        frequencies = []
        for key in dicts:
            frequencies.append((dicts[key], key))

        frequencies = sorted(frequencies, key=lambda x: x[0], reverse=True)
        ans = [frequency[1] for frequency in frequencies[:k]]
        return ans


nums = [1,1,1,2,2,3]
k = 2

nums = [1]
k = 1

nums = [1,1,1,2,2,3,3]
k = 2

solution = Solution()
print(solution.topKFrequent(nums, k))
