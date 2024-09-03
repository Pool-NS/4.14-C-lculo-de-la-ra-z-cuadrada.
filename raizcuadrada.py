import tkinter as tk
from tkinter import ttk
from math import sqrt


def calcular_raiz_cuadrada(a, iteraciones):
    x = 1.0
    resultados = []
    for _ in range(iteraciones):
        x = 0.5 * (x + a / x)
        resultados.append(x)
    return resultados


def calcular():
    try:
        a = float(entrada_a.get())
        iteraciones = int(entrada_iteraciones.get())
        if a < 0 or iteraciones < 1:
            raise ValueError("El valor debe ser positivo y el número de iteraciones debe ser al menos 1.")

        resultados = calcular_raiz_cuadrada(a, iteraciones)

        resultado_final = resultados[-1]
        etiqueta_resultado.config(text=f"La raíz cuadrada de {a} es aproximadamente {resultado_final:.10f}")

    except ValueError as e:
        etiqueta_resultado.config(text=f"Error: {e}")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Raíz Cuadrada")
ventana.geometry("400x200")

# Widgets
frame = ttk.Frame(ventana, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Valor de a:").grid(column=0, row=0, sticky=tk.W, pady=5)
entrada_a = ttk.Entry(frame, width=10)
entrada_a.grid(column=1, row=0, sticky=tk.W, pady=5)

ttk.Label(frame, text="Número de iteraciones:").grid(column=0, row=1, sticky=tk.W, pady=5)
entrada_iteraciones = ttk.Entry(frame, width=10)
entrada_iteraciones.grid(column=1, row=1, sticky=tk.W, pady=5)

ttk.Button(frame, text="Calcular", command=calcular).grid(column=0, row=2, columnspan=2, pady=10)

etiqueta_resultado = ttk.Label(frame, text="")
etiqueta_resultado.grid(column=0, row=3, columnspan=2, pady=5)

ventana.mainloop()


