class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        # construct difference array
        da = [0] * n

        for booking in bookings:
            da[booking[0] - 1] += booking[2]
            if booking[1] < n:
                da[booking[1]] -= booking[2]

        ans = list()
        seats = 0
        for item in da:
            seats += item
            ans.append(seats)
        return ans


bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5

bookings = [[1,2,10],[2,2,15]]
n = 2

solution = Solution()
print(solution.corpFlightBookings(bookings, n))
