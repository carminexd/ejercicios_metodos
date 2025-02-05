#   Codigo que implementa un esquema numerico 
#   para determinar la precision de una maquina
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025
#
import numpy as np
import matplotlib.pyplot as plt

epsilon = 1.0 
iteracion = 0

x = []  # Lista para almacenar iteraciones
y = []  # Lista para almacenar valores de epsilon

while 1.0 + epsilon != 1.0:
    epsilon /= 2
    iteracion += 1
    x.append(iteracion)
    y.append(epsilon)
    print(f"Iteración: {iteracion}, Precisión de máquina: {epsilon}")

# Se multiplica por 2 para obtener el último valor correcto
epsilon *= 2
print(f"Precisión de máquina final: {epsilon}")

plt.scatter(x, y)
plt.plot(x, y, linestyle='dashed', marker='o', color='b')  # Se añade una línea para mayor claridad

plt.title('Gráfica de Errores')
plt.xlabel('Iteración')
plt.ylabel('Precisión de máquina')
plt.yscale('log')  # Escala logarítmica para mejor visualización
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.show()
