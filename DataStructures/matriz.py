class SuperMatriz:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matriz = [[0 for i in range(columns)] for j in range(rows)]

    def set(self, row, column, value):
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns: raise Exception("Invalid row or column")
        self.matriz[row][column] = value

    def get(self, row, column):
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns: raise Exception("Invalid row or column")
        return self.matriz[row][column]