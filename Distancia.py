import math

#(t1,g1) e (t2,g2) sao a latitude e longitude de dois pontos da Terra
Rm = 6371.01

#referenceInfo
referenceLatitude = 0
referenceLongitude = 0
cityA = ""
cityB = ""

#Convert from x degrees to Radians:
#option1: x * ((math.pi)/180)
#option2: math.radians(x)

d = Rm * math.acos((math.sin(t1) * math.sin(t2)) + (math.cos(t1) * math.cos(t2) * math.cos(g1-g2)))

print("Type L:")
L = float(input()) #lenght
print("Type N:")
N = int(input()) #sideCount

def areaCalculator(N, L):
    area = (N * (L**2)) / (4 * math.tan((math.pi) / N))
    return area

print(areaCalculator(N, L))