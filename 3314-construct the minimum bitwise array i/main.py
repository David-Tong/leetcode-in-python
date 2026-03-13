class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = 10

        from collections import defaultdict
        dicts = defaultdict(int)
        s = set()
        s.add(1)
        dicts[1] = 0
        for x in range(L):
            base = 2 ** (x + 1)
            target = 2 ** (x + 2) - 1
            ns = set()
            if target not in s:
                ns.add(target)
                dicts[target] = base - 1
            for item in s:
                target = base + item
                if target not in dicts:
                    ns.add(target)
                    dicts[target] = base + dicts[item]
            s.update(ns)

        # process
        ans = list()
        for num in nums:
            if num not in dicts:
                ans.append(-1)
            else:
                ans.append(dicts[num])
        return ans


nums = [2,3,5,7]
nums = [11,13,31]
nums = [491, 827, 991]

solution = Solution()
print(solution.minBitwiseArray(nums))
