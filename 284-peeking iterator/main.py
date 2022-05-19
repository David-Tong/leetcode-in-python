class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.curr = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.curr

    def next(self):
        """
        :rtype: int
        """
        tmp = self.curr
        if self.iterator.hasNext():
            self.curr = self.iterator.next()
        else:
            self.curr = None
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curr:
            return True
        else:
            return False


list = [1, 2, 3]

iterator = PeekingIterator(iter(list))

print(iterator.next())
print(iterator.peek())
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
