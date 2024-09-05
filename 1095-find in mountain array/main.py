# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray(object):
    def __init__(self, array):
        self.array = array

    def get(self, index):
        """
        :type index: int
        :rtype int
        """
        return self.array[index]

    def length(self):
        """
        :rtype int
        """
        return len(self.array)


class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        def binarySearch(left, right, func):
            while left + 1 < right:
                middle = (left + right) // 2
                if func(middle):
                    right = middle
                else:
                    left = middle + 1
            if func(left):
                return left
            elif func(right):
                return right
            else:
                return -1
        # L
        L = mountain_arr.length()

        # search peak
        peak = binarySearch(1, L - 2, lambda x: mountain_arr.get(x) > mountain_arr.get(x + 1))

        # search left
        idx = binarySearch(0, peak, lambda x: mountain_arr.get(x) >= target)
        if idx != -1 and mountain_arr.get(idx) == target:
            return idx

        # search right
        idx = binarySearch(peak + 1, L - 1, lambda x: mountain_arr.get(x) <= target)
        if idx != -1 and mountain_arr.get(idx) == target:
            return idx

        return -1


array = [1,2,3,4,5,3,1]
target = 3

array = [0,1,2,4,2,1]
target = 3

array = [1,2,1]
target = 1

array = [1,5,6,7,8,9,12,10]
target = 10

array = [1,2,4,5,9,3]
target = 1

array = [3,5,3,2,0]
target = 0

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82]
target = 1

array = [1,5,2]
target = 0

mountain_arr = MountainArray(array)

solution = Solution()
print(solution.findInMountainArray(target, mountain_arr))
