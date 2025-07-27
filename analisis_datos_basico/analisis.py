import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore


# Cargar el archivo CSV

df = pd.read_csv('analisis_datos_basico/datos.csv')

# Scatter plot de col1 vs col2
plt.scatter(df['col1'], df['col2'])
plt.xlabel('col1')
plt.ylabel('col2')
plt.title('Scatter plot de col1 vs col2')
plt.show()

