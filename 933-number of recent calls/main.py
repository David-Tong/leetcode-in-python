class RecentCounter(object):

    def __init__(self):
        self.queue = list()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)

        from bisect import bisect_left
        if t - 3000 <= self.queue[0]:
            return len(self.queue)
        else:
            idx = bisect_left(self.queue, t - 3000)
            return len(self.queue) - idx


rc = RecentCounter()
print(rc.ping(1))
print(rc.ping(100))
print(rc.ping(3001))
print(rc.ping(3002))
print(rc.ping(3100))
