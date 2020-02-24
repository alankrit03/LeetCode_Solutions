class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort()
        total_sum = sum(digits)
        n = len(digits)
        if total_sum == 0:
            return '0'
        elif total_sum < 3:
            return ''
        elif total_sum % 3:
            if total_sum % 3 == 1:
                for i in range(n):
                    if digits[i] % 3 == 1:
                        digits[i] = -1
                        break
                else:
                    cnt = 0
                    for i in range(n):
                        if digits[i] % 3 == 2:
                            digits[i] = -1
                            cnt += 1
                            if cnt == 2: break
            else:
                for i in range(n):
                    if digits[i] % 3 == 2:
                        digits[i] = -1
                        break
                else:
                    cnt = 0
                    for i in range(n):
                        if digits[i] % 3 == 1:
                            digits[i] = -1
                            cnt += 1
                            if cnt == 2: break

        res = ''
        for i in range(n - 1, -1, -1):
            if digits[i] != -1:
                res = res + str(digits[i])

        return res