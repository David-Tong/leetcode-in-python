class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        from collections import defaultdict
        self.prices = defaultdict(int)

        from sortedcontainers import SortedList
        self.avails = defaultdict(SortedList)
        self.rents = SortedList()

        for shop, movie, price in entries:
            self.prices[(shop, movie)] = price
            self.avails[movie].add((price, shop))

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        if movie in self.avails:
            return [shop for _, shop in self.avails[movie][:5]]
        return list()

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.prices[(shop, movie)]
        self.avails[movie].remove((price, shop))
        self.rents.add((price, shop, movie))

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.prices[(shop, movie)]
        self.avails[movie].add((price, shop))
        self.rents.remove((price, shop, movie))

    def report(self):
        """
        :rtype: List[List[int]]
        """
        return [[shop, movie] for _, shop, movie in self.rents[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

"""
entries = [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]
mrs = MovieRentingSystem(3, entries)
print(mrs.search(1))
mrs.rent(0, 1)
mrs.rent(1, 2)
print(mrs.report())
mrs.drop(1, 2)
print(mrs.search(2))
"""

entries = [[13,6406,5183],[10,2926,931],[0,6424,7126],[0,4988,4028],[6,8295,7660],[16,4729,3008],[7,6349,8844],[1,6896,3047],[8,4693,3264],[13,1984,6267],[14,4544,5627],[21,6347,1327],[7,4932,3085],[16,5577,1542],[11,9549,2609],[5,8830,5502],[19,3157,6780],[1,7953,5964],[7,1882,6571],[18,9932,1146],[17,5985,2625],[19,8434,4176],[19,1762,3420],[13,2558,984],[4,4693,6178],[17,6347,3059],[17,5808,1467],[21,7778,1596],[1,47,7419],[15,646,8719],[10,1694,9782],[6,5577,5867],[11,6406,4180],[12,6347,7325],[1,1112,8378],[8,6750,3274],[12,531,8300],[8,7672,6253],[17,5551,6090],[14,4321,597],[16,8872,2453],[5,9630,3367],[7,8872,9900],[16,3238,5601],[9,9630,9659],[12,431,2143],[13,646,6596],[12,7953,1106],[17,1564,5806],[9,4988,2545],[20,3852,3190],[16,7953,7802],[19,646,7631],[21,9816,46],[11,7778,37]]
mrs = MovieRentingSystem(22, entries)
mrs.rent(1, 7953)
print(mrs.report())
mrs.drop(1, 7953)
mrs.rent(11,9549)
print(mrs.report())
print(mrs.report())
print(mrs.search(531))
mrs.rent(17,6347)
print(mrs.search(9998))
mrs.rent(12,431)
mrs.drop(11,9549)
print(mrs.report())
mrs.rent(9,9630)
print(mrs.report())
mrs.rent(12,6347)
mrs.rent(14,4321)
mrs.drop(9,9630)
print(mrs.report())
mrs.rent(0,4988)
mrs.rent(13,6406)
mrs.rent(11,7778)
print(mrs.report())
mrs.rent(8,4693)




