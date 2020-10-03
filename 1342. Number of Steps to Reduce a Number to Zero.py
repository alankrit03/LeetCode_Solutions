"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Approach 1:

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        if num % 2:
            return self.numberOfSteps(num - 1) + 1
        else:
            return self.numberOfSteps(num // 2) + 1



"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Approach 2:
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        num = bin(num)[2:]
        l = 0
        count = 0
        for x in num:
            l += 1
            if x == '1':
                count += 1

        return l - 1 + count