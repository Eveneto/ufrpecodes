xa0, ya0, xa1, ya1 = [int(coordenada) for coordenada in input().split()] 
xb0, yb0, xb1, yb1 = [int(coordenada) for coordenada in input().split()] 

if xb0 > xa1 or xa0 > xb1:
    print('0')
elif yb0 > ya1 or ya0 > yb1:
    print('0')
else:
    print('1')
