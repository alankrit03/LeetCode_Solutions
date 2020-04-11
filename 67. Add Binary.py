class Solution:
    def addBinary(self, a: str, b: str) -> str:
        list_a = [int(a[i]) for i in range(len(a) - 1, -1, -1)]
        list_b = [int(b[i]) for i in range(len(b) - 1, -1, -1)]

        if len(b) > len(a):
            list_a, list_b = list_b, list_a

        carry = 0
        i = 0
        ans = []
        len_b = len(list_b)
        for i in range(len(list_a)):

            if i < len_b:
                ans.append(str(carry ^ list_b[i] ^ list_a[i]))
                carry = 1 if carry + list_b[i] + list_a[i] > 1 else 0
            else:
                ans.append(str(carry ^ list_a[i]))
                carry = 1 if carry + list_a[i] > 1 else 0

        else:
            if carry:
                ans.append('1')

        return ''.join(ans[::-1])