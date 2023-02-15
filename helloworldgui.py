import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    # Leer el archivo de Excel
    df = pd.read_excel('D:\perros.xlsx', sheet_name='Sheet1')

    # Calcular la media y desviación estándar de la edad para cada raza
    medias = df.groupby('Raza')['Edad'].mean()
    desv_est = df.groupby('Raza')['Edad'].std()

    # Crear la gráfica de distribución normal
    fig, ax = plt.subplots()
    for raza in df['Raza'].unique():

        # Calcular la distribución normal para cada raza
        media = medias[raza]
        desv = desv_est[raza]
        x = np.linspace(media - 3*desv, media + 3*desv, 100)
        y = norm.pdf(x, media, desv)
        ax.plot(x, y, label=raza)

    # Configurar la gráfica
    ax.set_xlabel('Edad')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_title('Distribución normal de edad por raza')
    ax.legend()

    # Crear el objeto FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # Agregar el objeto canvas a la interfaz gráfica
    canvas.get_tk_widget().grid(row=1, column=0)

def show_graph():
    plot_graph()

root = tk.Tk()

# Agregar una etiqueta
label = tk.Label(root, text='Presiona el botón para mostrar la gráfica o para cerrar la ventana')
label.grid(row=0, column=0)

# Agregar un botón
button1 = tk.Button(root, text='Mostrar', command=show_graph)
button2 = tk.Button(root, text="Cerrar", command=root.destroy)
button1.grid(row=0, column=1)
button2.grid(row=0, column=3)

root.mainloop()
