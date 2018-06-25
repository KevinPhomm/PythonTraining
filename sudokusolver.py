
class SudokuSolver():

    def __init__(self, grid):
        self.grid = grid

    def __isMissingOnLine(self, number, line):
        for value in self.grid[line]:
            if number == value:
                return False
        return True

    def __isMissingOnColumn(self, number, column):
        for value in self.grid[column]:
            if number == value:
                return False
        return True

    def __isMissingInBlock(self, number, line, column):
        return NotImplemented

    def solve(self):
        self.__isValid(0)
        return self.grid

    def __isValid(self, position):
        if position == 81:
            return True

        line = position/9
        column = position%9
        if self.grid[line][column] != 0 :
            return self.__isValid(position+1)

        for numberTest in range(1,9): #test de tous les numbers possible
            if self.__isMissingOnLine(numberTest, line) and self.__isMissingOnColumn(numberTest, column) and self.__isMissingInBlock(numberTest, line, column):
                self.grid[line][column] = numberTest

                if self._isValid(position+1):
                    return True

        self.grid[line][column] = 0
        return False



