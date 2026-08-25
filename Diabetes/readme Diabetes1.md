En este archivo documentaremos los cambios realizados en los conjuntos de datos cardiacos.
# Diabetes1
    Cargamos las librerias
    Cargamos la base de datos y le asignamos el nombre de Diabetes1.
    vemos el tamanio del dataset con .shape, vemos que es de (229474,22)
    Vemos el las columnas, el tipo de vairable que son y datos faltantes con .info()
    Vemos si hay filas duplicadas con .drop_duplicates()
    Observamos un rsumen numerico con .describe()
    Observamos un rsumen estadistico en este caso seleccionamos una columna,"ChoCheck" con la misma funcion del apso anterior
    Vemos el tipo de variables de cada columna con .dtypes
    Por ultimo le pedimos a la ia que nos creara una tabla con la descripcion de las distintas variables