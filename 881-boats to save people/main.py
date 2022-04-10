class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people)
        left = 0
        right = len(people) - 1
        boat = 0
        while left <= right:
            if people[right] + people[left] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            boat += 1
        return boat


people = [1, 2]
limit = 3

people = [3, 2, 2, 1]
limit = 3

people = [3, 5, 3, 4]
limit = 5

solution = Solution()
print(solution.numRescueBoats(people, limit))
