class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import defaultdict
        dicts = defaultdict(int)

        left = 0
        right = 0
        while right < len(nums):
            dicts[nums[right]] += 1
            while dicts[nums[right]] > 1:
                if dicts[nums[left]] > 1:
                    if right - left <= k:
                        return True
                dicts[nums[left]] -= 1
                left += 1
            right += 1
        return False


nums = [1,2,3,1]
k = 3

#nums = [1,0,1,1]
#k = 1

#nums = [1,2,3,1,2,3]
#k = 2

nums = [1,3,2,1,2,3]
k = 2

solution = Solution()
print(solution.containsNearbyDuplicate(nums, k))
