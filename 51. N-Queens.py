def queens(row):
    if row == n:
        print_matrix()
        print()
        return 0

    for j in range(n):
        if is_queen_safe(row, j):
            arr[row][j] = 'Q'
            queens(row + 1)
            arr[row][j] = '.'


def is_queen_safe(row, j):
    temp=j
    k = j + 1
    j -= 1

    for i in range(row - 1, -1, -1):
        if j > -1:
            if arr[i][j] == 'Q':
                return False
            j -= 1

        if arr[i][temp] == 'Q': return False

        if k < n:
            if arr[i][k] == 'Q':
                return False
            k += 1
    else:
        return True


def print_matrix():
    for i in range(n):
        print(*arr[i])


n = int(input())
arr = [['.'] * n for i in range(n)]


queens(0)