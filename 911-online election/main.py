class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.L = len(times)
        self.persons = persons
        self.times = times
        self.tops = list()

        from collections import defaultdict
        votes = defaultdict(int)

        from heapq import heapify, heappush
        heap = list()
        heapify(heap)

        for x in range(self.L):
            votes[persons[x]] += 1
            heappush(heap, (votes[persons[x]] * -1, times[x] * -1, persons[x]))
            self.tops.append(heap[0][2])

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        from bisect import bisect_left
        idx = bisect_left(self.times, t)
        if idx == self.L:
            return self.tops[-1]
        elif self.times[idx] == t:
            return self.tops[idx]
        else:
            return self.tops[idx - 1]


persons = [0, 1, 1, 0, 0, 1, 0]
times = [0, 5, 10, 15, 20, 25, 30]

tvc = TopVotedCandidate(persons, times)
print(tvc.q(0))
print(tvc.q(3))
print(tvc.q(12))
print(tvc.q(25))
print(tvc.q(15))
print(tvc.q(24))
print(tvc.q(8))
print(tvc.q(35))
