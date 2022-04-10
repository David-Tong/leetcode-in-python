class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        if len(arr) % 2 != 0:
            return False

        from collections import defaultdict
        remains = defaultdict(int)

        for num in arr:
            remain = num % k
            remains[remain] += 1

        for remain in remains:
            if remain == 0:
                if remains[0] % 2 != 0:
                    return False
            else:
                if remains[remain] != remains[k - remain]:
                    return False
        return True


arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k = 5

arr = [1, 2, 3, 4, 5, 6]
k = 7

arr = [1, 2, 3, 4, 5, 6]
k = 10

arr = [7, 7]
k = 14

solution = Solution()
print(solution.canArrange(arr, k))
