class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for num in nums:
            dicts[num] += 1

        # process
        ans = 0
        for key in dicts:
            l = len(key)
            if key == target[:l]:
                other = target[l:]
                if other in dicts:
                    if key == other:
                        if dicts[key] > 1:
                            ans += dicts[key] * (dicts[key] - 1)
                    else:
                        ans += dicts[key] * dicts[other]
        return ans


nums = ["777","7","77","77"]
target = "7777"

nums = ["123","4","12","34"]
target = "1234"

nums = ["1","1","1"]
target = "11"

nums = ["11","11","11"]
target = "11"

nums = ["1","2","3"]
target = "11"

nums = ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
target = "11"

solution = Solution()
print(solution.numOfPairs(nums, target))
