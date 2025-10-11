import numpy as np
import matplotlib.pyplot as plt

# Datos
datosX = [0, 4, 8]
datosY = [5, 5, 8]

# Crea el gráfico de dispersión (scatter plot)
plt.scatter(datosX, datosY)

# Opcional: Personaliza el gráfico
plt.title("Mi Gráfico de Dispersión")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Muestra el gráfico
plt.show()