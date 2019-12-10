class temptest2:
    def __init__(self): #def __init__(self,x,y):
        self.a=0        #self.a=x
        self.b=1        #self.b=y 
t2=temptest2()
print(t2.a)
print(t2.b)
class temptest3:
    def __init__(self,x,y): 
        self.a=x        
        self.b=y         
    def distance(self,point_x,point_y):
        return  ((self.a-point_x)**2+(self.b-point_y)**2)**0.5 
t3=temptest3(6,8)
answer=t3.distance(0,0)
print(answer)