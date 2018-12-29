###9th
class Ninth:
    def __init__(self,num):
        self.s=str(num)
        self.s1=self.s[0]
        self.s2=self.s[-1]
        self.sum=int(self.s1) + int(self.s2)
    def result(self):
        print("The sum of the first and last digits of the number is:{}".format(self.sum))
out=Ninth(123)
out.result()

