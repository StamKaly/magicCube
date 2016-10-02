class MagicSquare:
    def __init__(self):
        self.magicSquare = None

    def mod(self, number):
        return number % self.numberInt

    def generateMagicSquare(self, rowsNumber):
        try:
            numberInt = int(rowsNumber)
            self.numberInt = numberInt
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

        # (c) Chris Gadzinski ;)
        self.magicSquare = [[self.mod(2 * j + i) + self.mod(j + i) * numberInt
            for i in range(numberInt)] for j in range(numberInt)]
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
    MagicSquare().generateAndPrintMagicSquare(2)
