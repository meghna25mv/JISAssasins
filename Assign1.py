###assignment1


class First:
    def __init__(self,num):

        self.z = 0
        self.o = 0
        self.e = 0
        self.r = num % 10

        while (self.r > 0):
            if self.r == 0:
                self.z = self.z + 1
            elif self.r % 2 == 0:
                self.e = self.e + 1
            else:
                self.o = self.o + 1
            num = int(num / 10)
            self.r = num % 10

    def result(self):
        print("number of zero: {} , number of odd numbers: {} ,number of even numbers : {}".format(self.z,self.o,self.e))
out=First(2415)
out.result()