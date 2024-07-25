import pandas as pd
import matplotlib.pyplot as plt

# Define the local file path
file_path = r'C:\Users\cntoj\Downloads\sales (1).csv'

data = pd.read_csv(file_path)
print(data.head())
print(data.info())
print(data.describe())

# Ventas totales por vendedor
ventas_por_vendedor = data.groupby('Vendor')['Revenue'].sum()
print('Ventas por vendedor')
print(ventas_por_vendedor)

data['Date'] = pd.to_datetime(data['Date'])
data['YearMonth'] = data['Date'].dt.to_period('M')
ventas_mensuales_por_categoria = data.groupby(['YearMonth', 'Category'])['Sales'].sum().reset_index()
print(ventas_mensuales_por_categoria.head())

# Opcional: Mostrar las ventas mensuales por categoría en un gráfico de barras con título
pivot_table = ventas_mensuales_por_categoria.pivot(index='YearMonth', columns='Category', values='Sales')
ax = pivot_table.plot(kind='bar', figsize=(14, 7), title='Ventas Mensuales por Categoría')
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas')
ax.legend(title='Categoría')

plt.show()