class Solution(object):
    def rotate(self, matrix):

        n = len(matrix)
        for i in range (n // 2):  #for outer loop , only traverse half
            for j in range (i , n-i-1):
                temp = matrix[i][j] 
                matrix [i][j] = matrix [n-1-j][i]   #left ki value top me 
                matrix[n-1-j][i] = matrix [n-1-i][n-1-j] #bottom ki value left me 
                matrix [n-1-i][n-1-j] = matrix[j][n-1-i] #right ki value bottom me 
                matrix[j][n-1-i] = temp #temp ki value right me 
