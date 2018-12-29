class Seventh:
    def __init__(self,num):
        self.s = 0
        self.r = int(num % 10)
        while(num>0):
            self.s=self.s + self.r
            num=int(num/10)
            self.r =int( num % 10)
    def result(self):
        print("SUM = {} ".format(self.s))
out = Seventh(123)
out.result()
