diction = {'2': 'abc',
           '3': 'def',
           '4': 'ghi',
           '6': 'mno',
           '5': 'jkl',
           '7': 'pqrs',
           '8': 'tuv',
           '9': 'wxyz'}


def letter_comb(st, i):
    if i == n:
        res.append(st)
        return 0
    temp = len(diction[string[i]])
    temp2 = diction[string[i]]

    for j in range(temp):
        letter_comb(st + temp2[j], i + 1)


string = input()
res = []
n = len(string)
letter_comb('', 0)
print(*res)
