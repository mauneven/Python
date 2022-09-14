## Librerias y modulos

import math
import numpy as np
import pandas as pd

## Variables

df = pd.DataFrame()
x = float (0);
iteraciones = 10;
ax = 0.1;

## Ecuación

f = float((math.sin(x))-(4*x)+3);

## Obteniendo datos

for i in range (iteraciones):
    x = x+ax;
    f = float((math.sin(x))-(4*x)+3);
    print (f"para x = {x} | tiene el resultado = {f}");
    

xi = 0.9;
xu = 1;
xr = float((xi+xu)/2);
fi = float((math.sin(xi))-(4*xi)+3);
fu = float((math.sin(xu))-(4*xu)+3);
fr = float((math.sin(xr))-(4*xr)+3);
fifr = float(fi*fr);

df = pd.DataFrame(columns=['Xi', 'Xu', 'Xr', 'f(Xi)', 'f(Xu)', 'f(Xu)', 'f(Xr)', 'f(Xi)(Xr)'])

while (fifr > 0):

    fi = math.sin(xi)-(4*xi)+3;
    fu = math.sin(xu)-(4*xu)+3;
    fr = math.sin(xr)-(4*xr)+3;
    
    if (fifr < 0):
        xi = xi;

    else:
        xi = xr

    if (fifr < 0):
        xu = xr

    else:
        xu = xu
    
    print (fifr)

df = pd.DataFrame(columns=['Xi', 'Xu', 'Xr', 'f(Xi)', 'f(Xu)', 'f(Xu)', 'f(Xr)', 'f(Xi)(Xr)'])

print (fifr)



