import matplotlib.pyplot as plt
import numpy as np

# Definir los parámetros
precio_unitario = 10  # Precio de venta por unidad
costo_fijo = 1000  # Costo fijo total
costo_variable_unitario = 5  # Costo variable por unidad

# Crear un rango de unidades producidas
unidades = np.arange(0, 200)

# Calcular los ingresos totales
ingresos = precio_unitario * unidades

# Calcular los costos totales
costos_variables = costo_variable_unitario * unidades
costos_totales = costos_fijos + costos_variables

# Crear la gráfica
plt.plot(unidades, ingresos, label='Ingresos')
plt.plot(unidades, costos_totales, label='Costos Totales')
plt.xlabel('Unidades Producidas')
plt.ylabel('Monto ($)')
plt.title('Punto de Equilibrio')
plt.legend()
plt.grid(True)
plt.show()
