class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 5:
            return False

        sum_ = 1
        root = math.ceil(num ** .5)
        print(root)
        for i in range(2, root):
            if num % i == 0:
                sum_ += i
                if i != root:
                    sum_ += num // i

        return sum_ == num