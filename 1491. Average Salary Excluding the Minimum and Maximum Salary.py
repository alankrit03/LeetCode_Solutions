class Solution:
    def average(self, salary: List[int]) -> float:
        min_ = salary[0]
        max_ = salary[0]
        ans = -(2 * min_)
        i = 0
        for x in salary:
            if x > max_:
                ans += max_
                max_ = x
            elif x < min_:
                ans += min_
                min_ = x
            else:
                ans += x
            i += 1

        return ans / (i - 2)