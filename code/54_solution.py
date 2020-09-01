class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and matrix[0] + self.spiralOrder(self.ccw_rotate(matrix[1:]))

    @staticmethod
    def ccw_rotate(matrix):
        return list(map(list, zip(*(map(reversed, matrix)))))
