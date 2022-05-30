class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        from heapq import heapify
        self.n = n
        self.heap = [_ + 1 for _ in range(self.n)]
        heapify(self.heap)

    def reserve(self):
        """
        :rtype: int
        """
        from heapq import heappop
        return heappop(self.heap)


    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        from heapq import heappush
        heappush(self.heap, seatNumber)


seat_manager = SeatManager(5)
print(seat_manager.reserve())
print(seat_manager.reserve())
seat_manager.unreserve((2))
print(seat_manager.reserve())
print(seat_manager.reserve())
print(seat_manager.reserve())
print(seat_manager.reserve())
seat_manager.unreserve(5)
