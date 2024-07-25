import pandas as pd
import matplotlib.pyplot as plt

# Define the local file path
file_path = r'C:\Users\cntoj\Downloads\BD_johnny.xlsx'

df = pd.read_excel(file_path, sheet_name='BD')
print(df.head())
df['Fecha'] = pd.to_datetime(df['Fecha'])
administracion_df = df[df['Rubro'] == 'Administración']
administracion_df['AñoMes'] = administracion_df['Fecha'].dt.to_period('M')
gastos_administracion_mensuales = administracion_df.groupby('AñoMes')['Transaccion'].sum().reset_index()
print(gastos_administracion_mensuales)

plt.figure(figsize=(12, 6))
plt.bar(gastos_administracion_mensuales['AñoMes'].astype(str), gastos_administracion_mensuales['Transaccion'])
plt.title('Gastos de Administración Mensuales')
plt.xlabel('Mes')
plt.ylabel('Gasto')
plt.xticks(rotation=45)
plt.show()