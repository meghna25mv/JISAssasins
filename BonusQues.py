##BONUS QUESTION
import random
class BonusQues:

    def __init__(self,user):
        self.n=random.randint(1000,9999)
        self.user=user
        self.cow = 0
        self.bull = 0
        self.l1=[]
        self.l2=[]
        self.r1 = self.n % 10
        self.r2 = user % 10
        while(self.r1>0):
            self.r1 = self.n % 10
            self.l1.append(self.r1)
            self.r1 = int(self.r1/10)
        while (self.r2 > 0):
            self.r2 = user % 10
            self.l2.append(self.r2)
            self.r2 = int(self.r2 / 10)


            for items in self.l1:
                if items in self.l2:
                    self.cow=self.cow+1
                else:
                    self.bull=self.bull+1

    def result(self):
        print("cow = {} and bull ={}".format(self.cow,self.bull))
value=BonusQues(1234)
value.result()