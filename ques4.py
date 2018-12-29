####Ques4
class Fourth:
    def __init__(self,n):
        self.l = []
        for i in range(n):
            self.num=int(input("enter the value "))
            self.l.append(self.num)
        (self.l).sort()
    def result1(self):
        print("Sorted value is {} ".format(self.l))
out=Fourth(5)
out.result1()

