buildings= []
temp = []
H=[]
W=[]

''' Code to take input starts here'''
def tempLength(temp):
    if len(temp)== 4:
        buildings.append(temp.copy())
        temp.clear()
        

while True:
    cordinate = list(map(float, input().strip().split(",")))
    tempLength(temp)
    if len(cordinate) < 2: ##To break the input stream when cordinates are entered please enter an integer##
        break
    else:
        W.append(cordinate[0])
        H.append(cordinate[1])
        temp.append(cordinate)

''' Code to take input ends here'''

source = list(map(float, input().strip().split(",")))
'''input cordinates are reversed so that smallest building comes firts'''
H.reverse()
W.reverse()

'''To calculate the area exposed to sunlight when only one building is present'''
def SurfaceArea(source,H,W,y):
    if source[1] >= max(H):
        roof = abs(abs(max(W)) - abs(min(W)))
        side = abs(abs(max(H)) - abs(y))
    
    return roof+side

'''To calculate the slope of line between the source and the max(cordinates) of firts building''' 
def slope(source, x2, y2):
    # Here x2 & y2 is the cordinates of first building
    x1,y1 = source[0], source[1]
    return ((y2-y1)/(x2-x1))
'''Calculates the y cordinate of the second building intersected by sunray'''
def calY(source, x1, y1, x2): 
    # Here x1 & y1 is the cordinate of first building
    # and x2 is cordinate of next building
    s = slope(source, x1, y1) 
    return ((s*(x2-x1))+y1) # returns value of y2

'''Calculates the total area exposed to sunlight due to all the buildings by adding
    surface area of firts building'''
def totalSurface(source, H,W):
    no_building=len(H)//4
    previousSum = 0
    Htemp = []
    Wtemp = []
    

    tempCordinate = [min(W[:4]),min(H[:4])]

    for i in range(len(H)):
       
        Htemp.append(H[i])
        Wtemp.append(W[i])
        if len(Htemp) == 4:
       
            nextCordinate = min(Wtemp)
            y = calY(source, tempCordinate[0], tempCordinate[1], nextCordinate)
            previousSum += SurfaceArea(source,Htemp,Wtemp,y)
            
            if no_building > 1:
                tempCordinate = [max(Wtemp),max(Htemp)]
            
            Htemp.clear()
            Wtemp.clear()
    print(previousSum)

        
    
totalSurface(source, H,W)



