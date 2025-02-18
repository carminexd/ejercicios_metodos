import numpy as np
import matplotlib.pyplot as plt

# Definir la función g(x) para el método de punto fijo
def g(x):
    return np.exp(x) / 4

# Criterio de convergencia (opcional, se puede usar la condición del error absoluto)
def g_prime(x):
    return np.exp(x) / 4

# Error absoluto
def error_absoluto(x_new, x_old):
    return abs(x_new - x_old)

# Método de punto fijo
def punto_fijo(x0, tol=1e-5, max_iter=100):
    iteraciones = []
    errores_abs = []

    x_old = x0
    for i in range(max_iter):
        x_new = g(x_old)
        e_abs = error_absoluto(x_new, x_old)

        iteraciones.append((i+1, x_new, e_abs))
        errores_abs.append(e_abs)

        if e_abs < tol:
            break

        x_old = x_new

    return iteraciones, errores_abs

# Parámetros iniciales
x0 = 1.0
iteraciones, errores_abs = punto_fijo(x0)

# Imprimir tabla de iteraciones
print("Iteración | x_n       | Error absoluto")
print("---------------------------------------")
for it in iteraciones:
    print(f"{it[0]:9d} | {it[1]:.6f} | {it[2]:.6e}")

# Graficar la convergencia
x_vals = np.linspace(0, 3, 100)  # Ajusta el rango según sea necesario
y_vals = g(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r"$g(x) = e^x / 4$", color="blue")
plt.plot(x_vals, x_vals, linestyle="dashed", color="red", label="y = x")

# Graficar iteraciones
x_points = [it[1] for it in iteraciones]
y_points = [g(x) for x in x_points]
plt.scatter(x_points, y_points, color="black", zorder=3)
plt.plot(x_points, y_points, linestyle="dotted", color="black", label="Iteraciones")

plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.grid(True)
plt.title("Método de Punto Fijo")
plt.savefig("punto_fijo_convergencia.png")
plt.show()

# Graficar errores
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(errores_abs) + 1), errores_abs, marker="o", label="Error absoluto")

plt.xlabel("Iteración")
plt.ylabel("Error")
plt.yscale("log")  # Escala logarítmica para mejor visualización
plt.legend()
plt.grid(True)
plt.title("Evolución del Error Absoluto")
plt.savefig("errores_punto_fijo.png")
plt.show()