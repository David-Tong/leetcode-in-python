class ProductOfNumbers(object):

    def __init__(self):
        self.nums = list()
        self.products = list()

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        # process nums
        self.nums.append(num)

        # process products
        if self.products:
            self.products.append(self.products[-1] * num)
        else:
            self.products.append(num)

        idx = len(self.products) - 2
        idx2 = 0
        while idx >= 0:
            if self.nums[idx2] == 0:
                self.products[idx] = 1
                for x in range(idx + 1):
                    self.products[idx] *= self.nums[-(x + 1)]
            else:
                self.products[idx] = self.products[idx] // self.nums[idx2] * num
            idx -= 1
            idx2 += 1

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        return self.products[k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

pon = ProductOfNumbers()
pon.add(3)
pon.add(0)
pon.add(2)
pon.add(5)
pon.add(4)
print(pon.getProduct(2))
print(pon.getProduct(3))
print(pon.getProduct(4))
pon.add(8)
print(pon.getProduct(2))
