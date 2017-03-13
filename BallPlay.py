'''
Created on 2016年8月4日

@author: Anshare_LY
'''
import sys            
class Ballplay():
    def __init__(self):self.BallHit=[];self.BallScore=0    
    def hit(self,HitBall):self.BallHit.append(HitBall)
    def reset(self):self.BallHit.clear();self.BallScore=0
    def getScore(self):
        BallFlag=True;BallRound=0;i=0
        while BallFlag :
            if  i==len(self.BallHit)-1: self.BallHit.append(0)
            if self.BallHit[i]==10 : #and BallRound < 11:
                self.BallScore+=self.BallHit[i]+self.BallHit[i+1]+self.BallHit[i+2]
                BallRound=BallRound+1
                i=i+1
            elif self.BallHit[i]!=10 and self.BallHit[i]+self.BallHit[i+1]==10:
                self.BallScore+=self.BallHit[i]+self.BallHit[i+1]+self.BallHit[i+2]
                BallRound=BallRound+1
                i=i+2
            elif self.BallHit[i]!=10 :
                self.BallScore+=self.BallHit[i]+self.BallHit[i+1]
                BallRound=BallRound+1
                i=i+2              
            if  BallRound>= 10 or i>=len(self.BallHit):
                BallFlag=False
        return self.BallScore

  
if __name__ == '__main__':
    BP=Ballplay()
    BP.reset()
    BP.hit(5)
    BP.hit(4)
    print("正确得分：9 我的计算结果： " + str(str(BP.getScore())))
    BP.reset()
    BP.hit(5)
    BP.hit(4)
    BP.hit(7)
    BP.hit(2)
    print("正确得分：18 我的计算结果： " + str(BP.getScore()))
    BP.reset()
    BP.hit(3)
    BP.hit(7)
    BP.hit(3)
    print("正确得分：16 我的计算结果： " + str(BP.getScore()))
    BP.reset()
    BP.hit(3)
    BP.hit(7)
    BP.hit(3)
    BP.hit(2)
    print("正确得分：18 我的计算结果： " + str(BP.getScore()))
    BP.reset()
    BP.hit(10)
    BP.hit(3)
    BP.hit(6)
    print("正确得分：28 我的计算结果： " + str(BP.getScore()))
    BP.reset()
    for i in range(0,12) : 
        BP.hit(10)
    print("正确得分：300 我的计算结果： " + str(BP.getScore()))
    BP.reset()
    for i in range(0,9):
        BP.hit(0)
        BP.hit(0)
    BP.hit(2)
    BP.hit(8)
    BP.hit(10)
    print("正确得分：20 我的计算结果： " + str(BP.getScore()))
    BP.reset()
    BP.hit(1)
    BP.hit(4)
    BP.hit(4)
    BP.hit(5)
    BP.hit(6)
    BP.hit(4)
    BP.hit(5)
    BP.hit(5)
    BP.hit(10)
    BP.hit(0)
    BP.hit(1)
    BP.hit(7)
    BP.hit(3)
    BP.hit(6)
    BP.hit(4)
    BP.hit(10)
    BP.hit(2)
    BP.hit(8)
    BP.hit(6)
    print("正确得分：133 我的计算结果： " + str(BP.getScore()))
    BP.reset()
    for i in range(0,11): 
        BP.hit(10)
    BP.hit(9)
    print("正确得分：299 我的计算结果： " + str(BP.getScore()))
    BP.reset()
    for i in range(0,9): 
        BP.hit(10)
    BP.hit(9)
    BP.hit(1)
    BP.hit(1)
    print("正确得分：270 我的计算结果： " + str(BP.getScore()))
    
