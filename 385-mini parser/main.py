class NestedInteger(object):
    pass


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        def getNumber(nums):
            if isinstance(nums, int):
                return NestedInteger(nums)
            lst = NestedInteger()
            for num in nums:
                lst.add(getNumber(num))
            return lst
        return getNumber(eval(s))


s = "[123,[456,[789]]]"
s = "[456,[789]]"
s = "[789]"

print(eval(s))

nums = eval(s)
for num in nums:
    print(num)

solution = Solution()
#print(solution.deserialize(s))
