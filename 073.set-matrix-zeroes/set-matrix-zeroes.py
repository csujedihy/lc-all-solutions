class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        colZeroFlag = False
        for i in xrange(0, len(matrix)):
            if matrix[i][0] == 0:
                colZeroFlag = True
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        
        for i in reversed(xrange(0, len(matrix))):
            for j in reversed(xrange(1, len(matrix[0]))):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if colZeroFlag:
                matrix[i][0] = 0
                
                
        