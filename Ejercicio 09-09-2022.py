import math
import numpy as np
import pandas as pd

iteraciones = 10;
xi = 0
xu = 5
xr = (xi+xu)/2;
fi = (math.pow(xi,2)*abs(math.cos(math.sqrt(xi))))-5
fu = (math.pow(xu,2)*abs(math.cos(math.sqrt(xu))))-5
fr = (math.pow(xr,2)*abs(math.cos(math.sqrt(xr))))-5
fifr = fi*fr

df = pd.DataFrame()

for i in range (iteraciones):

    fi = (math.pow(xi,2)*abs(math.cos(math.sqrt(xi))))-5
    fu = (math.pow(xu,2)*abs(math.cos(math.sqrt(xu))))-5
    fr = (math.pow(xr,2)*abs(math.cos(math.sqrt(xr))))-5
    fifr = (fi*fr)
       
    if (fifr < 0):
        xi = xi
    else:
        xi = xr
        
    if (fifr < 0):
        xu = xr
    else:
        xu = xu
        
    xr = (xi+xu)/2
    
    df['Xi'] = xi
    
    print (xi)
