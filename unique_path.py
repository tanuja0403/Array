class Solution (object):
    def uniquePaths(self , m , n ):
        grid = []
        for i in range(m):
            row = [1]* n 
            grid.append(row)

        for row in range (1 , m ):
            for col in range (1 , n):
                grid[row][col] = grid[row-1][col] + grid[row][col-1]

        return grid[m-1][n-1]



    