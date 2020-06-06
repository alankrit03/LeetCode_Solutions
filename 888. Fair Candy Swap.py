class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        set_b = set(B)
        sum_a = sum(A)
        sum_b = sum(B)

        equal_sum = (sum_a + sum_b) // 2

        for ele in A:
            req = sum_b + ele - equal_sum
            if req > 0 and req in set_b:
                return [ele, req] 