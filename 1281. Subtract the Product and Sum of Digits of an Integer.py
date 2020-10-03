class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        k = n
        sum_ = 0
        while k:
            d = k % 10
            prod *= d
            sum_ += d
            k //= 10

        return prod - sum_