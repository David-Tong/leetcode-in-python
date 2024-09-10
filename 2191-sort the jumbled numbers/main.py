class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def mapNum(num):
            mapped = ""
            for digit in str(num):
                mapped += str(mapping[int(digit)])
            return int(mapped)

        pairs = list()
        for idx, num in enumerate(nums):
            pairs.append((mapNum(num), idx, num))
        pairs = sorted(pairs, key=lambda x: (x[0], x[1]))

        ans = [_[2] for _ in pairs]
        return ans


mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]

mapping = [0,1,2,3,4,5,6,7,8,9]
nums = [789,456,123]

solution = Solution()
print(solution.sortJumbled(mapping, nums))
