
class SudokuSolver():

    def __init__(self, grid):
        self.grid = grid

    def __isMissingOnLine(self, number, line):
        for i in range(0, 9):
            if number == self.grid[line][i]:
                return False
        return True

    def __isMissingOnColumn(self, number, column):
        for i in range(0,9):
            if number == self.grid[i][column]:
                return False
        return True

    def __isMissingInBlock(self, number, line, column):
        blockindexline = self.__getBlockRange(line/3)
        blockindexcolumn = self.__getBlockRange(column/3)

        for i in blockindexline :
            for j in blockindexcolumn :
                if number == self.grid[i][j]:
                    return False
        return True

    def solve(self):
        self.__isValid(0)


    def __getBlockRange(self,blockindex):
        if blockindex < 1 :
            return [0,1,2]
        if blockindex < 2 :
            return [3,4,5]
        if blockindex < 3 :
            return [6,7,8]

    def __isValid(self, position):
        if position == 81:
            return True

        line = position//9
        column = position%9

        if self.grid[line][column] != 0 :
            return self.__isValid(position+1)

        for numberTest in range(1,10): #test de tous les numbers possible
            if self.__isMissingOnLine(numberTest, line) and self.__isMissingOnColumn(numberTest, column) and self.__isMissingInBlock(numberTest, line, column):
                self.grid[line][column] = numberTest
                if self.__isValid(position+1):
                    return True

        self.grid[line][column] = 0
        return False




sudoku = [[0,8,5,0,7,0,0,0,0],
          [0,6,0,0,0,4,0,0,0],
          [3,0,1,6,0,0,0,0,4],

          [0,0,0,8,0,7,0,5,0],
          [1,0,0,0,0,0,0,0,6],
          [0,5,0,3,0,1,0,0,0],

          [5,0,0,0,0,9,3,0,7],
          [0,0,0,1,0,0,0,2,0],
          [0,0,0,0,4,0,8,9,0]]

sudokuObject = SudokuSolver(sudoku)
sudokuObject.solve()
print(sudokuObject.grid)

