import numpy as np
import matplotlib.pyplot as plt

def calcular_errores(x, y, valor_real):
    diferencia = x - y
    error_abs = abs(valor_real - diferencia)
    error_rel = error_abs / abs(valor_real)
    error_pct = error_rel * 100
    return error_abs, error_rel, error_pct

# Datos
valores = [(1.000000000000001, 1.000000000000000, 0.0000001), (1.000000000000001, 1.000000000000, 0.000000000001)]
error_abs_list = []
error_rel_list = []
error_pct_list = []
labels = []

for i, (x, y, real) in enumerate(valores):
    error_abs, error_rel, error_pct = calcular_errores(x, y, real)
    error_abs_list.append(error_abs)
    error_rel_list.append(error_rel)
    error_pct_list.append(error_pct)
    labels.append(f"Caso {i+1}")

# Gráfica
x = np.arange(len(valores))  # Posiciones en el eje x
width = 0.2  # Ancho de las barras

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, error_abs_list, width, label='Error Absoluto')
rects2 = ax.bar(x, error_rel_list, width, label='Error Relativo')
rects3 = ax.bar(x + width, error_pct_list, width, label='Error Porcentual')

# Etiquetas y título
ax.set_xlabel('Casos')
ax.set_ylabel('Valores de error')
ax.set_title('Comparación de errores')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Mostrar la gráfica
plt.show()