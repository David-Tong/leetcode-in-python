class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        from collections import defaultdict
        baskets = defaultdict(int)

        ans = 0
        while right < len(fruits):
            baskets[fruits[right]] += 1
            right += 1

            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1

            ans = max(ans, right - left)
        return ans


fruits = [1,2,1]
fruits = [0,1,2,2]
fruits = [1,2,3,2,2]
fruits = [1]
fruits = [1,2,3,2,2,4,4,6,4,4,6,6]

solution = Solution()
print(solution.totalFruit(fruits))
