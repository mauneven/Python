## Librerias y modulos

from itertools import count
import math
from math import ceil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



## Variables

df = pd.DataFrame()
x = float (0);
i = int(input("Ingrese el numero de iteraciones: "));
ax = float(input("En cuantos decimales desea que x se aumente: "));
data = []
columnas = ['xi', 'xu', 'xr', 'fi', 'fu', 'xr', 'f(xi)*f(xu)']

## Ecuación

f = float((math.sin(x))-(4*x)+3);

## Print

for i in range (0, i):
    x = x+ax;
    f = float((math.sin(x))-(4*x)+3);
    print (f"para x = {x} | tiene el resultado = {f}");

xi = float(input("Segun los resultado obtenidos cual es el valor de su xi: "));
xu = float(input("Segun los resultados obtenidos cual es el valor de su xu: "));
xr = float((xi+xu)/2);

print(f"El valor de su xr es {xr}")

for i in range (0, i):
    fi = float((math.sin(xi))-(4*xi)+3);
    fu = float((math.sin(xu))-(4*xu)+3);
    fr = float((math.sin(x))-(4*x)+3);
    fifr = fi*fr;

    if ( fr < 0):
        xi = xi

    else:
        xi = xr

data =[i, xi, xu, xr, fi, fu, fr, fifr]
tabla = pd.DataFrame(data, columns = columnas)

print (tabla)

