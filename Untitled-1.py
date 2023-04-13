# %%
import pandas as pd
import matplotlib as plt
import seaborn as sns


# %% [markdown]
# 

# %%
df_base_de_datos = pd.read_csv("base-de-datos-gto.csv")
df_base_de_datos.head()


# %%
df_base_de_datos.shape

# %%
#Categorias y numéricas

df_base_de_datos.info()

# %%
df_base_de_datos.dtypes

# %%
df_base_de_datos.isnull().sum()

# %%
df_base_de_datos.columns

# %%
df_base_de_datos.info

# %%
# Eliminar columnas con valores faltantes en el DataFrame original
df_base_de_datos.dropna(axis=1, inplace=True)
# Imprimir información del DataFrame modificado
df_base_de_datos.info()


# %%

# Crear un nuevo DataFrame sin valores faltantes
df_sin_faltantes = df_base_de_datos.dropna(inplace=False)
# Imprimir información del nuevo DataFrame
df_sin_faltantes.info()


# %%
df_base_de_datos.describe()

# %%
import matplotlib.pyplot as plt

# Cargar datos desde archivo Excel
df_freq = pd.read_csv('freq.csv')


# %%
# Crear gráfico de barras
df_freq.hist(figsize=(5, 10))

# %%
df_freq = pd.read_csv('freq.csv')
df_freq.head

# %%
df_base_de_datos.head()

# %%
#df_base_de_datos

# utilizar el método transpose
df_transpuesto = df_base_de_datos.transpose()

# utilizar la función T
df_T = df_base_de_datos.T

print(df_base_de_datos)
print(df_transpuesto)
print(df_T)


# %%
df_T.head()


# %%
df_T.to_csv('describe.csv', sep=',')

# %%
df_T.dtypes

# %%
df_T.index.name = "Preguntas"
df_T.head

# %%
df_T.isnull()

# %%

df_describe = pd.read_csv('describe.csv')
resultados_df_T = pd.DataFrame(columns=df_describe.columns)

for i in range(len(df_describe)):
    conteos = df_describe.iloc[i].value_counts()
    resultados_df_T = resultados_df_T.append(conteos, ignore_index=True)

print(resultados_df_T)

# %%
df_freq = resultados_df_T.describe().T  # Transponer el DataFrame

for row in df_freq.index:
    plt.bar(df_freq.columns, df_freq.loc[row])
    plt.title(row)
    plt.show()

# %%
df_freq=resultados_df_T.describe()
print(df_freq)
for column in df_freq.columns:
    plt.bar(df_freq.index, df_freq[column])
    plt.title(column)
    plt.show()


# %%
df_freq=resultados_df_T.describe()
print(df_freq)


