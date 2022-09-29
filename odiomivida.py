import math
import numpy as np
import pandas as pd

iteraciones = 10;
xi = 0.9 
xu = 1
xr = (xi+xu)/2;
fi = math.sin(xi)-(4*xi)+3
fu = math.sin(xu)-(4*xu)+3
fr = math.sin(xr)-(4*xr)+3
fifr = fi*fr

df = pd.DataFrame()

for i in range (iteraciones):

    fi = math.sin(xi)-(4*xi)+3
    fu = math.sin(xu)-(4*xu)+3
    fr = math.sin(xr)-(4*xr)+3
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
    
    print (fifr)
