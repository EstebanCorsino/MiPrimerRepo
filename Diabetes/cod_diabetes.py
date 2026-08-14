import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Diabetes = pd.read_csv("Diabetes/cdc_diabetes_data.csv")
print(Diabetes.iloc[:10, :10])  # primeras 10 filas y 10 columnas
Diabetes.head
Diabetes.shape
Diabetes.drop_duplicates()
print(Diabetes.drop_duplicates())
# sin duplicados Diabetes1
Diabetes1 = Diabetes.drop_duplicates()
print(Diabetes1.shape)
print("\nTotal de nulos en la base:")
print(Diabetes1.isnull().sum().sum())
print(Diabetes1.dtypes)
# para ver una descripcion de los datos de la columna BMI
print(Diabetes1["BMI"].describe())




