class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        original = sum(flowerbed)

        index = 0
        while index < len(flowerbed):
            if index == 0 and flowerbed[0] == 0:
                flowerbed[0] = 1
            else:
                if flowerbed[index - 1] == 0:
                    flowerbed[index] = 1
            index += 1

        index = len(flowerbed) - 1
        while index > 0:
            if flowerbed[index] == 1 and flowerbed[index - 1] == 1:
                flowerbed[index - 1] = 0
            index -= 1

        updated = sum(flowerbed)

        if n <= updated - original:
            return True
        else:
            return False


flowerbed = [1, 0, 0, 0, 1]
n = 1
n = 2

solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))