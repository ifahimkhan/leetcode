class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            next_row = [1] + [None] * (i - 1) + [1]
            for j in range(1, len(next_row) - 1):
                next_row[j] = row[j-1] + row[j]
            row = next_row
        return row
