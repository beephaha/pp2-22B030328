class beep:
    def __init__(self):
        self.string=""
    def getString(self):
        self.string = input()
    def PrintString(self):
        print((self.string).upper())


obj = beep()
obj.getString()
obj.PrintString()