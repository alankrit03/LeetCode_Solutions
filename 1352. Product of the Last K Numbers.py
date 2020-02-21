class ProductOfNumbers:

    def __init__(self):
        self.list1 = []
        self.zero_occur = []
        self.productlist = []
        self.product=1
    def add(self, num: int) -> None:
        self.list1.append(num)
        if num==0:
            self.zero_occur.append(len(self.list1)-1)
            self.productlist.append(self.product)
        else:
            self.product *= num
            self.productlist.append(self.product)

    def getProduct(self, k: int) -> int:
        n=len(self.list1)
        if self.zero_occur and self.zero_occur[-1] >= n-k :
            return 0
        elif k==n:
            return self.product
        else:
            return self.product // self.productlist[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)