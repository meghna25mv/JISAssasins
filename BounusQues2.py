###Bonus Ques
import random
class BonusQues2:
    def __init__(self,user):
        self.c=0
        self.n = random.randint(100000, 999999)
        self.user = user
        while(self.n != self.user):
            self.n=random.randint(100000,999999)

            self.c=self.c+1
    def result(self):
            print("The total number of attemps : {}".format(self.c))
out=BonusQues2(333333)
out.result()