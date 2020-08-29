class Solution:
    def nthUglyNumber(self, n: int) -> int:
        starts = [0, 0, 0]
        numbers = [1]
        k = 1
        while k < n:
            a = numbers[starts[0]]
            b = numbers[starts[1]]
            c = numbers[starts[2]]

            new_num = min(a * 2, b * 3, c * 5)

            if not new_num % 2:
                starts[0] += 1

            if not new_num % 3:
                starts[1] += 1

            if not new_num % 5:
                starts[2] += 1

            numbers.append(new_num)
            k += 1

        return numbers[n - 1]