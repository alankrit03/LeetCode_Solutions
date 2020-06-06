class Solution:
    def myAtoi(self, str: str) -> int:
        ans_str = ''
        cache = set('0987654321')
        str = str.lstrip()
        print(str)
        for x in str:
            if x in cache:
                ans_str += x
            elif x in ('-', '+'):
                if len(ans_str):
                    break
                else:
                    ans_str += x
            else:
                break

        try:
            ans = int(ans_str)
        except:
            return 0

        return min(max(-2 ** 31, ans), 2 ** 31 - 1)
