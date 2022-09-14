# Se importan librerias

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Se define la variable

def evaluaFuncion (pFuncion, pValor):
    variable = "@x"
    return eval(pFuncion.replace(variable, pValor))


# Print para inicializar

print ("MÉTODO GRÁFICO")
print ()
print ("Ingrese la función")
fx = input()
print ("Digite el valor de x")
x = float(input())
print ("Digite el valor de las iteraciones")
iteraciones = int(input())
print()

data = []
columnas = ["x", "f(x)"]
pltX = []
pltFx = []

for i in range (0, iteraciones):
    funcion = evaluaFuncion(fx, str(x))
    pltX.append(x)
    pltFx.append(funcion)
    data.append([x, "{:.4f}".format(funcion)])
    x += 1
    
## solo prints

tabla = pd.DataFrame(data, columns = columnas)
print(tabla)

print()
plt.plot(pltX, pltFx, label=fx, color = "tab:blue")
plt.title(fx)
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Funcion")
plt.xticks()
plt.legend()
plt.show()

print ("MÉTODO BISECCIÓN")
print ()

print ("Ingrese la función")
fx = input()

print ("Digite el valor de xi")
xi = float(input())

print ("Digite el valor de xu")
xu = float(input())

print ("Digite el valor de la raiz")
raiz = float(input())

print ("Digite el valor de las iteraciones")
iteraciones = int(input())

print()

data = []
columnas = ['Xi', 'Xu', 'Xr', 'f(xi)', 'f(xu)', 'f(Xr)', 'f(Xi)*f(Xr)', 'Et(%)', 'Ea(%)']

xr = 0 ## pa que no arroje error

for i in range (0, iteraciones):
    antxr = xr
    xr = (xi+xu)/2
    fxi = evaluaFuncion(fx, str(xi))   
    fxu = evaluaFuncion(fx, str(xu))
    fxr = evaluaFuncion(fx, str(xr))
    fxi_fxr = fxi*fxr
    
    et = abs((raiz-xr)/raiz)*100
    
    if (i ==0):
        ea = 0
        
    else:
        ea = abs((xr-antxr)/xr)*100
        
    data.append(["{:.9f}".format(xi), "{:.9f}".format(xu), "{:.9f}".format(xr), "{:.9f}".format(fxi), "{:.9f}".format(fxu), "{:.9f}".format(fxr), "{:.9f}".format(fxi_fxr), "{:.9f}".format(et), "{:.9f}".format(ea)])
        
    if fxi_fxr < 0:
        xu = xr
    else: 
        xi = xr
    
print ()

tabla = pd.DataFrame(data, columns = columnas)
print (tabla)