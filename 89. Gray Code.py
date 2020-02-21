n = int(input())
list1 = [0, 1]

if n > 1:
    temp = 1
    for i in range(1, n):
        temp = 2 * temp
        list2 = []
        for x in list1:
            list2.append(x + temp)
        list2.reverse()
        list1.extend(list2)

print(*list1)