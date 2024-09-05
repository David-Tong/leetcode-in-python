class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        # search the largest number make sum less or equal to the target
        def lteTarget(pivot, target):
            total = 0
            for item in arr:
                if item > pivot:
                    total += pivot
                else:
                    total += item
            if total > target:
                return False
            else:
                return True

        left = 0
        right = max(arr)

        while left + 1 < right:
            middle = (left + right) // 2
            if lteTarget(middle, target):
                left = middle
            else:
                right = middle - 1

        if lteTarget(right, target):
            low = right
        else:
            low = left

        # search the least number make sum greater or equal to the target
        def gteTarget(pivot, target):
            total = 0
            for item in arr:
                if item > pivot:
                    total += pivot
                else:
                    total += item
            if total < target:
                return False
            else:
                return True

        left = 0
        right = max(arr)

        while left + 1 < right:
            middle = (left + right) // 2
            if gteTarget(middle, target):
                right = middle
            else:
                left = middle + 1

        if gteTarget(left, target):
            high = left
        else:
            high = right

        def getGap(pivot, target):
            total = 0
            for item in arr:
                if item > pivot:
                    total += pivot
                else:
                    total += item
            return abs(target - total)

        low_gap = getGap(low, target)
        high_gap = getGap(high, target)
        return low if low_gap <= high_gap else high


arr = [4,9,3]
target = 10

arr = [2,3,5]
target = 10

arr = [60864,25176,27249,21296,20204]
target = 56803

arr = [11]
target = 1

solution = Solution()
print(solution.findBestValue(arr, target))
