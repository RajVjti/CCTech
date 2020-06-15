import math as m

'''The test point class starts here'''
class Point():
    def __init__(self,h,v):
        self.h=h
        self.v=v
'''The test point class ends here'''

'''Computes the sum of angle made between test point and each pair of points
    making up the angle'''
def InsidePolygon(polygon,n,p):
    i=0
    angle=0
    p1=Point(0,0)
    p2=Point(0,0)
    for i in range (0,n):
        p1.h = polygon[i].h - p.h;
        p1.v = polygon[i].v - p.v;
        p2.h = polygon[(i+1)%n].h - p.h;
        p2.v = polygon[(i+1)%n].v - p.v;
        angle += Angle2D(p1.h,p1.v,p2.h,p2.v);
'''function ends here'''
'''checks if angle is less than 2*pi then inside otherwise outside'''
    if(abs(angle)<=2*m.pi):
        return ("FALSE")
    else:
        return("TRUE")

'''calculates the differnce of angle between angles'''
def Angle2D(x1,y1,x2,y2):
    theta1=m.atan2(y1,x1)
    theta2=m.atan2(y2,x2)
    dtheta=theta2-theta1
    return(dtheta)


'''code to take input'''  
polygon=[Point(-3,2),Point(-2,-0.8),Point(0,1.2),Point(2.2,0),Point(2,4.5)]
n=len(polygon)
p=Point(0,0)
print(InsidePolygon(polygon,n,p))
