class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.items = self.__flattenList(nestedList)
        self.N = len(self.items)
        self.idx = 0

    def next(self):
        """
        :rtype: int
        """
        item = self.items[self.idx]
        self.idx += 1
        return item

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < self.N

    def __flattenList(self, lst):
        items = []
        for item in lst:
            if item.getInteger() is not None:
                items.append(item)
            else:
                items.extend(self.__flattenList(item.getList()))
        return items


nestedList = [[1,1],2,[1,1]]
nestedList = [1,[4,[6]]]
iter = NestedIterator(nestedList)

while iter.hasNext():
    print(iter.next())
