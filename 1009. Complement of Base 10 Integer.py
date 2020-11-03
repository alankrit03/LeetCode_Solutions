class Solution:
    def bitwiseComplement(self, N: int) -> int:
        st = bin(N)[2:]
        temp = ''
        for x in st:
            if x == '1':
                temp += '0'
            else:
                temp += '1'

        return int(temp, 2)
