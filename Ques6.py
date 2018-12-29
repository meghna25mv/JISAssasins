class Sixth:
    def __init__(self):
        self.l = []
        for i in range(5):
            self.names = input("enter the names ")
            self.l.append(self.names)
        (self.l).sort()

    def result1(self):
        print("Sorted names are {} ".format(self.l))


out = Sixth()
out.result1()