class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

s = StringManipulator()
s.getString()
s.printString()
