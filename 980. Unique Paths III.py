"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
path=0
def uniquePathsIII(grid):

    def check_fullgrid():
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==0 :
                    return False
        else:return 1

    def travel_path(i,j):
        global path
        if i==n or j==m or i==-1 or j==-1 or grid[i][j] == -1:
            return 0

        if grid[i][j] == 2:
            if check_fullgrid():
                path+=1
            return 0

        if grid[i][j] == 1:
            grid[i][j] = -1
            travel_path(i - 1, j)
            travel_path(i + 1, j)
            travel_path(i, j - 1)
            travel_path(i, j + 1)
            grid[i][j] = 1
        else:
            grid[i][j]=-1
            travel_path(i-1,j)
            travel_path(i+1,j)
            travel_path(i,j-1)
            travel_path(i,j+1)
            grid[i][j]=0

    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                source = (i,j)
    travel_path(source[0] , source[1])

    return path


grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
n_paths = uniquePathsIII(grid)
print(n_paths)