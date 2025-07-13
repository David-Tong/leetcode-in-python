class Solution(object):
    def minimumNumbers(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        dicts[0] = [0, 0]
        plural, target, unit = 1, k, k
        while unit not in dicts:
            dicts[unit] = [plural, target]
            plural += 1
            target = plural * k
            unit = target % 10
        # conner case : num = 3000, k = 9
        if unit == 0:
            dicts[10] = [plural, target]

        print(dicts)

        # process
        unit = num % 10
        if unit in dicts:
            # conner case : num = 3000, k = 9
            if unit == 0 and num > 0:
                plural, target = dicts[10]
            else:
                plural, target = dicts[unit]
            if num < target:
                return -1
            else:
                return plural
        else:
            return -1

num = 58
k = 9

num = 37
k = 2

num = 0
k = 7

num = 3000
k = 9

solution = Solution()
print(solution.minimumNumbers(num, k))
