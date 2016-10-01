__author__ = 'Stam Kaly'
__date__ = '30-9-2016'

class MagicSquare:
    def __init__(self):
        self.magicSquare = None

    def generateMagicSquare(self, rowsNumber):
        try:
            numberInt = int(rowsNumber)
        except ValueError:
            print("You can generate a Magic Square only with a NUMBER of rows!")
            self.magicSquare = None
            return None
        if numberInt == 1:
            self.magicSquare = 1
            return 1
        elif numberInt <= 0:
            print("You can't generate any squares with 0 or less number of rows!")
            self.magicSquare = None
            return None
        self.rowsNumber = numberInt
        self.finalNumber = numberInt*numberInt

        # Magnetic Duck's version following this https://en.wikipedia.org/wiki/Magic_square#Method_for_constructing_a_magic_square_of_odd_order :
        self.magicSquare = [[((2 * j + 1 + i) % numberInt) + ((6 + i + j) % numberInt) * numberInt + 1 for i in range(numberInt)] for j in range(numberInt)]


        '''
        This is my version following the algorithm shown here http://puzzling.stackexchange.com/a/1982 :


        unacceptableNumbers = ['0', '2', '4', '6', '8']
        for number in unacceptableNumbers:
            if str(rowsNumber).endswith(number):
                print("Sorry you can generate a Magic Square only with uneven number of rows!")
                self.magicSquare = None
                return None


        self.magicSquare = []
        for _ in range(numberInt):
            row = []
            for _ in range(numberInt):
                row.append(0)
            self.magicSquare.append(row)
        self.magicSquare[0][int(numberInt/2-0.5)] = 1
        currentNumber = 2
        currentRow = 0
        currentColumn = int(numberInt/2-0.5)
        for _ in range(self.finalNumber - 1):
            workingRow = currentRow
            workingColumn = currentColumn
            workingRow -= 1
            workingColumn += 1
            if workingRow < 0:
                workingRow = numberInt - 1
            if workingColumn > numberInt - 1:
                workingColumn = 0
            if self.magicSquare[workingRow][workingColumn] == 0:
                self.magicSquare[workingRow][workingColumn] = currentNumber
                currentRow = workingRow
                currentColumn = workingColumn
            else:
                if currentRow + 1 > numberInt - 1:
                    currentRow = 0
                else:
                    currentRow += 1
                self.magicSquare[currentRow][currentColumn] = currentNumber
            currentNumber += 1
        '''
        return self.magicSquare

    def printMagicSquare(self):
        if self.magicSquare == None:
            return
        elif self.magicSquare == 1:
            print("|\u0305\u03321\u0305\u0332|\u0305\u0332")
        else:
            for magicRow in self.magicSquare:
                row = ""
                if self.magicSquare.index(magicRow) == self.rowsNumber - 1:
                    extraCharacter = "\u0332"
                else:
                    extraCharacter = ""
                for magicNumber in magicRow:
                    row += "|\u0305{}".format(extraCharacter)
                    if len(str(magicNumber)) == len(str(self.finalNumber)):
                        for number in str(magicNumber):
                            row += "{}\u0305{}".format(number, extraCharacter)
                    else:
                        spaces = len(str(self.finalNumber)) - len(str(magicNumber))
                        for _ in range(spaces):
                            row += "\u203E{}".format(extraCharacter)
                        for number in str(magicNumber):
                            row += "{}\u0305{}".format(number, extraCharacter)
                print("{}|\u0305{}".format(row, extraCharacter))
            self.magicSquare = None


    def generateAndPrintMagicSquare(self, rowsNumber):
        self.generateMagicSquare(rowsNumber)
        self.printMagicSquare()



if __name__ == '__main__':
    MagicSquare().generateAndPrintMagicSquare(3)
