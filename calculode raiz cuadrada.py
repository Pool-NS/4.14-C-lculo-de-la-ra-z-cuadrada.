import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calcular_raiz_cuadrada(a, iteraciones):
    x = 1.0
    resultados = []
    for k in range(1, iteraciones + 1):
        x = 0.5 * (x + a / x)
        resultados.append(x)
    return resultados


def actualizar_grafica(resultados):
    ax.clear()
    ax.plot(range(1, len(resultados) + 1), resultados, marker='o')
    ax.set_xlabel('Iteraciones')
    ax.set_ylabel('Valor de la raíz')
    ax.set_title('Convergencia de la Raíz Cuadrada')
    canvas.draw()


def calcular():
    try:
        a = float(entrada_a.get())
        iteraciones = int(entrada_iteraciones.get())
        if a < 0 or iteraciones < 1:
            raise ValueError

        resultados = calcular_raiz_cuadrada(a, iteraciones)

        resultado_final = resultados[-1]
        etiqueta_resultado.config(text=f"La raíz cuadrada de {a} es aproximadamente {resultado_final:.10f}")

        actualizar_grafica(resultados)

    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingrese valores válidos.")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Raíz Cuadrada")
ventana.geometry("600x500")

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

# Configuración de la gráfica
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=0, padx=10, pady=10)

