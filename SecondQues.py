###Ques2

class Second:
    def __init__(self,n):
        self.l = []
        for i in range(n):
            self.num=int(input("enter the value "))
            self.l.append(self.num)
        self.max=max(self.l)
        self.min=min(self.l)
    def result(self):
        print("Maximum value is {} and minimum value is {}".format(self.max,self.min))
out=Second(10)
out.result()