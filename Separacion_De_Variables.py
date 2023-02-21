import numpy as np
import matplotlib.pyplot as plt

# Definir la ecuación diferencial
def f(x, y):
    return -(8*x+5)/(3*y**2+1)

# Definir la función para resolver la ecuación diferencial
def separacion_variables(y0, x0):
    # Definir el rango de la variable independiente
    x = np.linspace(-5, 5, 1000)
    # Aplicar el método de separación de variables
    y = np.sqrt((3*y0**2+1)/3)*np.exp(-2*x**2-5*x)
    # Ajustar la solución para satisfacer el valor inicial
    C = y0/np.sqrt((3*y0**2+1)/3)*np.exp(2*x0**2+5*x0)
    y = y*C
    return x, y

# Trazar las curvas de nivel
fig, ax = plt.subplots(figsize=(8,6))
for y0, x0 in [(-1,0), (2,0), (4,-1), (-3,-1)]:
    x, y = separacion_variables(y0, x0)
    ax.plot(x, y, label=f'y({x0})={y0}')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
