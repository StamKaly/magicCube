__author__ = 'Stam Kaly'
__date__ = '30-9-2016'

class MagicCube:
    def __init__(self):
        self.magicCube = None

    def generateMagicCube(self, rowsNumber):
        try:
            numberInt = int(rowsNumber)
        except ValueError:
            print("You can generate a Magic Cube only with a NUMBER of rows!")
            self.magicCube = None
            return None
        unacceptableNumbers = ['0', '2', '4', '6', '8']
        if numberInt == 1:
            self.magicCube = 1
            return 1
        elif numberInt <= 0:
            print("You can't generate any cubes with 0 or less number of rows!")
        for number in unacceptableNumbers:
            if str(rowsNumber).endswith(number):
                print("Sorry you can generate a Magic Cube only with uneven number of rows!")
                self.magicCube = None
                return None


        self.finalNumber = numberInt * numberInt
        self.magicCube = []
        for _ in range(numberInt):
            row = []
            for _ in range(numberInt):
                row.append(0)
            self.magicCube.append(row)
        self.magicCube[0][int(numberInt/2+0.5) - 1] = 1
        currentNumber = 2
        currentRow = 0
        currentColumn = int(numberInt/2+0.5) - 1
        for _ in range(self.finalNumber - 1):
            workingRow = currentRow
            workingColumn = currentColumn
            workingRow -= 1
            workingColumn += 1
            if workingRow < 0:
                workingRow = numberInt - 1
            if workingColumn > numberInt - 1:
                workingColumn = 0
            if self.magicCube[workingRow][workingColumn] == 0:
                self.magicCube[workingRow][workingColumn] = currentNumber
                currentRow = workingRow
                currentColumn = workingColumn
            else:
                if currentRow + 1 > numberInt - 1:
                    currentRow = 0
                else:
                    currentRow += 1
                self.magicCube[currentRow][currentColumn] = currentNumber
            currentNumber += 1
        return self.magicCube


    def printMagicCube(self):
        if self.magicCube == None:
            return
        elif self.magicCube == 1:
            print(u"|\u03051\u0305|\u0305\n \u0305 \u0305 \u0305")
        else:
            for magicRow in self.magicCube:
                row = ""
                for magicNumber in magicRow:
                    row += "|\u0305"
                    if len(str(magicNumber)) == len(str(self.finalNumber)):
                        for number in str(magicNumber):
                            row += "{}\u0305".format(number)
                    else:
                        spaces = len(str(self.finalNumber)) - len(str(magicNumber))
                        for _ in range(spaces):
                            row += " \u0305"
                        for number in str(magicNumber):
                            row += "{}\u0305".format(number)
                rowLength = len("{}|\u0305".format(row))
                print(u"{}|\u0305".format(row))
            finalLine = ""
            for _ in range(int(rowLength/2)):
                finalLine += " \u0305"
            print(u"{}".format(finalLine))
            self.magicCube = None


    def generateAndPrintMagicCube(self, rowsNumber):
        self.generateMagicCube(rowsNumber)
        self.printMagicCube()



if __name__ == '__main__':
    MagicCube().generateAndPrintMagicCube(13)
