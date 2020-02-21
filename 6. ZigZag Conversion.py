class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # print(s)

        if numRows == 1:
            return s

        factor = (numRows - 1) * 2
        # print(factor)

        new_str = ''

        for i in range(numRows):
            n = len(s)
            j = i
            flag = True
            second_factor = (i) * 2

            # print(f'i {i} , second_factor {second_factor}')

            if i == 0 or i == numRows - 1:
                while j < n:
                    new_str += s[j]
                    j += factor
            else:
                while j < n:
                    new_str += s[j]

                    if flag:
                        j += factor - second_factor
                        flag = False
                    else:
                        j += second_factor
                        flag = True

        # print(new_str)
        return new_str