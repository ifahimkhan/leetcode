class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        in place using bitwise not
        """
        n = len(matrix)
        for i in range(n - n // 2):
            for j in range(n // 2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                              matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
